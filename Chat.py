import os
import time
from google import genai
import httpx
import json
from datetime import datetime, date
from google.genai import types
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

daily_limit = 100
tracker_path = "tracker.json"
today = str(date.today())

# retrieves api keys from .env file for security
sc_api_key = os.getenv("SEARCH_API_KEY")
gsearch_engine_id = os.getenv("SEARCH_ENGINE_ID")

gemini_logo = "assets\Google_Gemini_logo_2025.png"
st.logo(gemini_logo)

st.title("Chat with Gemini")

user_input = st.chat_input("What is the weather like tomorrow in Srinagar?",
                           key="user prompt")

# reads and returns history.json file
def load_hist(filename="history.json"):
    if os.path.exists("history.json") and os.path.getsize("history.json") > 0:
        try:
            with open("history.json", "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            st.write("Corrupted JSON file.")
    return []

history = load_hist()

def add_hist(prompt, response):
    global history
    history.append({"prompt":prompt, "response":response})
    with open("history.json","w", encoding="utf-8") as f:
        json.dump(history, f, indent=4, ensure_ascii=False)

# performs the google search using Custom Search JSON API
def googlesearch(api_key, search_engine_id, query, **params):
        query = query.strip()
        if not query:
            raise ValueError("Search query cannot be empty.")

        base_url = 'https://www.googleapis.com/customsearch/v1'
        params = {
            'key': api_key,
            'cx': search_engine_id,
            'q': query,
            **params
        }
        response = httpx.get(base_url, params=params)
        response.raise_for_status()
        return response.json()

# searches the web and adds important information from web to a string
search_output = ""

def search_content():
    global search_output
    search_results = googlesearch(sc_api_key, gsearch_engine_id, user_input)
    items = search_results.get("items", [])

    if not items:
        st.write("⚠️No search results found")
    else:
        for index, row in enumerate(items[:5],start=1):
            search_output += f"[{index}] {row.get('title','No title')} ({row.get('link','')})\n{row.get('snippet','No description available')}\n\n"

# Example of how search snippets look like, before passing to Gemini
# Enter your prompt: Weather today in delhi
# [1] 10-day weather forecast for Rajpath Area, Delhi - The Weather ... (https://weather.com/en-IN/weather/tenday/l/Rajpath+Area+Delhi?canonicalCityId=61622bd7864baeacb900e507db46f6ef)
# 10-Day Weather-Rajpath Area, Delhi. As of 15:23 IST. Tonight. --/26°. 4%. Night. 26°. 4%. NW 12 km/h. Generally clear. Low 26°C. Winds NW at 10 to 15 km/h.

# [2] Delhi, Delhi, India Weather Forecast | AccuWeather (https://www.accuweather.com/en/in/delhi/202396/weather-forecast/202396)
# Delhi, Delhi, India Weather Forecast, with current conditions, wind, air quality, and what to expect for the next 3 days.

# [3] Weather forecast and conditions for Rajpath Area, Delhi - The ... (https://weather.com/en-IN/weather/today/l/Rajpath+Area+Delhi?canonicalCityId=61622bd7864baeacb900e507db46f6ef)
# Rajpath Area, Delhi Forecast · Today · Hourly · Daily. Morning. 32°. -- · Afternoon. 34°. -- · Evening. 30°. Chance of Rain1% · Overnight. 27°. Chance ...

# passing contents to Gemini API, configuring the model and returns the response

if os.path.exists(tracker_path):
    with open(tracker_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {}
else:
    data = {}

prev_date = data.get("date_prompt")
if prev_date != today:
    exec_count = 0
else:
    exec_count = data.get("exec_count", 0)

# Updated track_usage function
def track_usage(filename=tracker_path):
    global exec_count
    exec_count += 1
    with open(filename, "w", encoding="utf-8") as f:
        json.dump({"exec_count": exec_count, "date_prompt": today}, f, indent=2, ensure_ascii=False)


def gemini(model_name):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    # storing history.json as string
    history_text = load_hist()

    # instruction to gemini to use search output and history access, in order to answer the user query
    system_prompt = f"""
    Context from web: {search_output}
    Here is the full chat history in JSON format:
    {str(history_text)}
    User asked: {user_input}
    Answer clearly. Use web context when it’s relevant.
    If the web context does not contain the answer, you may rely on your own knowledge,
    and dont mention web sources then.
    Format answer such that most important information is at the top i.e in order of relevance and importance
    """

    try:
        response = client.models.generate_content(

            # gemini model
            model=model_name,

            # content passed to the model
            contents = user_input,

            # configuring the model
            config=types.GenerateContentConfig(
                system_instruction=system_prompt, # passing the instructions
                temperature=1, # controls creativity
                seed=3, # for consistent answers
                safety_settings=[
                    types.SafetySetting(
                        category="HARM_CATEGORY_HATE_SPEECH",
                        threshold="BLOCK_ONLY_HIGH",
                    )
                ],
            ),
        )
        add_hist(user_input, response.text)
        track_usage("tracker.json")
        return response.text
    except Exception as e:
        st.write("Some Error occurred:", e)

col1, col2 = st.columns(2)

with col1:
    search_on = st.toggle("Enable Google Search")

with col2:
    model_name = st.selectbox(
        "Model",
        ("gemini-2.5-flash-lite", "gemini-2.5-flash", "gemini-2.5-pro"),
        width=250,
    )

def stream_response(response):
    for word in response.split(" "):
        yield word + " "  # Yield the word followed by a space
        time.sleep(0.05)

if user_input:
    if search_on:
        search_content()
    with st.chat_message("assistant", avatar="assets\image.png"):
        try:
            gemini_response = gemini(model_name)
            st.write_stream(stream_response(gemini_response))
            st.caption(f"{daily_limit - exec_count} prompts remaining today")
        except Exception as e:
            st.write("Some Error occurred:", e)


if exec_count >= daily_limit:
    st.write("Daily limit reached")
    st.stop()







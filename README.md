# Chat with Gemini

A Gemini Chatbot Web Application made in Python using Google's Gemini API and Custom Search JSON API, and streamlit library to create and deploy the web app

## Setup

1. Cloning the repository
git clone https://github.com/vj031206/gemini-chat-in-python.git
cd gemini-chat-in-python

2. Creating a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Create a .env file in the root directory, based on .env.example:
GEMINI_API_KEY=YOUR_KEY_HERE
SEARCH_API_KEY=YOUR_KEY_HERE
SEARCH_ENGINE_ID=YOUR_KEY_HERE

Get keys for
Gemini API:
Custom Search JSON API:
Search Engine ID: 

5. Run the app
streamlit run Chat.py

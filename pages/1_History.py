import streamlit as st
import json
import os

st.title("History")

if st.button("Clear History"):
    with open("history.json", "w") as f:
        f.write("[]")
    st.caption("History cleared!")

if os.path.exists("history.json") and os.path.getsize("history.json") > 0:
    try:
        with open("history.json", "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        st.write("Corrupted JSON file.")
        data = []
else:
    data = []


if not data:
    st.write("Start Chatting ......")
else:
    for row in data:
        label = f"{row.get('prompt', 'No prompt')}"
        expander = st.expander(label)
        expander.write(row.get("response", "No response"))
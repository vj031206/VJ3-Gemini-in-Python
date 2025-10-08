# Chat with Gemini

A Gemini Chatbot Web Application made in Python using Google's Gemini API and Custom Search JSON API, and streamlit library to create and deploy the web app.

Use Google Search results with just a simple toggle
View your chat history in the history tab, expand on any of your prompts to view the full response
Choose the gemini model you want to use

![2025-10-08 11 48 23 localhost 0782699b3427](https://github.com/user-attachments/assets/c3cde95e-f4e8-4ea9-8969-92a412414d85)
![2025-10-08 11 49 00 localhost fc28a0e7f7ee](https://github.com/user-attachments/assets/4a55f91f-e19b-42fe-a71a-d7af67fca9ea)
![2025-10-08 11 49 45 localhost dc61d47c41a9](https://github.com/user-attachments/assets/559dc3a9-c424-4a8d-9e51-8ed1172dc683)
![2025-10-08 11 50 24 localhost 5114d0edc02a](https://github.com/user-attachments/assets/4ee5cf9d-a105-47f9-815b-24c5377a1922)
![2025-10-08 11 50 12 localhost 2b2021c869d9](https://github.com/user-attachments/assets/c0595733-f236-4607-9c6f-6dacc12dff99)



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

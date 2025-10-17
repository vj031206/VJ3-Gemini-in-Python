# 🤖 Gemini Chatbot in Python

A feature-rich chatbot web application built with Python using Google's Gemini API, Custom Search JSON API, and the Streamlit library. This project was developed as part of the Codexintern Python Developer internship.

-----

## ✨ Features

  * **🌐 Integrated Google Search**: Seamlessly toggle Google Search to get real-time information within your chats.
  * **📚 Chat History**: Easily view and revisit your past conversations in the history tab. Expand any prompt to see the full response.
  * **🧠 Model Selection**: Choose the specific Gemini model you want to interact with from a dropdown menu.

-----

## 📸 Screenshots

Here's a glimpse of the application in action:

| Chat Interface | Chat History |
| :---: | :---: |
| ![2025-10-08 11 48 23 localhost 0782699b3427](https://github.com/user-attachments/assets/c3cde95e-f4e8-4ea9-8969-92a412414d85) | ![2025-10-08 11 50 24 localhost 5114d0edc02a](https://github.com/user-attachments/assets/4ee5cf9d-a105-47f9-815b-24c5377a1922) |

| Google Search Toggle | Model Selection |
| :---: | :---: |
| ![2025-10-08 11 49 45 localhost dc61d47c41a9](https://github.com/user-attachments/assets/559dc3a9-c424-4a8d-9e51-8ed1172dc683) | <img width="1920" height="1080" alt="Screenshot (89)" src="https://github.com/user-attachments/assets/33827ad1-b7c0-4d91-90c4-f7d46725c1af" /> |

-----

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

### 1\. Clone the Repository

First, clone the repository to your local machine.

```bash
git clone https://github.com/vj031206/gemini-chat-in-python.git
cd gemini-chat-in-python
```

### 2\. Create and Activate a Virtual Environment

It's recommended to create a virtual environment to manage dependencies.

  * **On Linux/macOS:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
  * **On Windows:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

### 3\. Install Dependencies

Install all the required Python packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4\. Set Up Environment Variables

You'll need to provide API keys for Google's services.

1.  Create a new file named `.env` in the root directory of the project.

2.  Copy the contents of `.env.example` into your new `.env` file.

3.  Add your API keys to the `.env` file:

    ```env
    GEMINI_API_KEY="YOUR_KEY_HERE"
    SEARCH_API_KEY="YOUR_KEY_HERE"
    SEARCH_ENGINE_ID="YOUR_KEY_HERE"
    ```

<!-- end list -->

  * **Gemini API Key**: Get yours from [Google AI Studio](https://aistudio.google.com/welcome).
  * **Custom Search JSON API Key & Search Engine ID**: Follow the instructions on the [Google Custom Search API page](https://developers.google.com/custom-search/v1/introduction).

### 5\. Run the Application

Once the setup is complete, you can run the Streamlit app with the following command:

```bash
streamlit run Chat.py
```

Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

-----

## 📁 Other Projects

Feel free to check out my other projects:

  * **Speech-to-Image Generator**: [vj031206/VJ3-Speech-to-Image](https://github.com/vj031206/VJ3-Speech-to-Image.git)
  * **Sentiment Analyser**: [vj031206/VJ3-Sentiment-Analysis-flask](https://github.com/vj031206/VJ3-Sentiment-Analysis-flask.git)

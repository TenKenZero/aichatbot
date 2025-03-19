# AI Chatbot Application

## Overview

This project is a simple chatbot web application built using the Django framework in Python. It allows users to interact with AI models from OpenAI and Google to get responses to their text and image-based queries. The application features user authentication, chat history, and the ability to send images to the AI for processing.

## Features

* **User Authentication:** Users can register, log in, and log out to secure their chat history.
* **Chat Interface:** A clean and intuitive interface for real-time interaction with the chatbot.
* **Message History:** The application stores and displays the user's previous chat history.
* **AI Integration:** Utilizes both OpenAI and Google AI APIs to provide intelligent responses.
* **Text and Image Input:** Users can send both text messages and upload images for the AI to process.
* **Clear History:** Logged-in users have the option to clear their chat history.

## Technologies Used

* **Django:** A high-level Python web framework.
* **Python:** The primary programming language.
* **psycopg2:** PostgreSQL database adapter for Python.
* **OpenAI API:** For generating responses based on text input.
* **Google Generative AI:** For handling both text and image-based queries.
* **HTML, CSS, and Bootstrap:** For the frontend structure and styling.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd aichatbot
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Linux/macOS
    venv\Scripts\activate.bat  # On Windows
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requeriments.txt
    ```
    This will install the necessary libraries including Django, psycopg2, openai, and google-generativeai.
4.  **Set up the database:**
    * Ensure you have PostgreSQL installed and running.
    * Create a database for the project.
    * Update the database settings in `aichatbot/settings.py` with your database credentials.
5.  **Apply migrations:**
    ```bash
    python manage.py migrate
    ```
6.  **Create a superuser (optional but recommended for admin access):**
    ```bash
    python manage.py createsuperuser
    ```
7.  **Obtain API Keys:**
    * You will need API keys for OpenAI and Google AI.
    * Refer to the respective API documentation for instructions on how to obtain them.
    * Set these API keys as environment variables or directly in the `chatbot/openAIAPI.py` and `chatbot/googleAPI.py` files.

## Usage

1.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
2.  **Access the application:** Open your web browser and navigate to `http://127.0.0.1:8000/`.
3.  **Register or Login:** New users will need to register before using the chatbot. Existing users can log in with their credentials.
4.  **Start chatting:** Once logged in, you will be directed to the chatbot interface where you can type your messages and send them. You can also attach images using the "Attach Image" button. The chatbot's response will appear in the chat window.
5.  **Clear History:** You can clear your chat history by clicking on the "Clear History" link.
6.  **Logout:** To logout, click on the "Logout" link.

## Project Structure
```
aichatbot/
├── chatbot/
│   ├── admin.py
│   ├── apps.py
│   ├── googleAPI.py     # Handles interactions with the Google AI API
│   ├── migrations/
│   │   └── ...
│   ├── models.py        # Defines the database models
│   ├── openAIAPI.py     # Handles interactions with the OpenAI API
│   ├── tests.py
│   ├── urls.py          # Defines URL patterns for the chatbot app
│   └── views.py         # Handles the application logic and views
├── templates/
│   ├── base.html        # Base HTML template
│   ├── chatbot.html     # Chatbot interface template
│   ├── login.html       # Login page template
│   └── register.html    # Registration page template
├── staticfiles/
│   └── ...            # Static files (CSS, JavaScript, etc.)
├── manage.py            # Django management script
├── requeriments.txt     # Project dependencies
├── settings.py          # Django project settings
├── urls.py              # Main project URL patterns
├── asgi.py
└── wsgi.py
```

## Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them.
4.  Push your changes to your fork.
5.  Submit a pull request.

## License

MIT
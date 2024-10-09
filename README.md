# Flask Authentication App

This is a simple Flask application that demonstrates user authentication using Flask, Flask-SQLAlchemy, and Flask-Bcrypt.

## Features

- User registration
- User login
- User dashboard (protected route)
- User logout

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Bcrypt
- SQLite

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/flask-authentication-app.git
    cd flask-authentication-app
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the application:**

    ```bash
    python app.py
    ```

6. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:5000`.

## Project Structure

- `app.py`: The main application file containing routes and logic.
- `templates/`: Directory containing HTML templates.
- `static/`: Directory containing static files (CSS, JavaScript, images).
- `requirements.txt`: File listing the dependencies.

## Routes

- `/`: Home page.
- `/register`: User registration page.
- `/login`: User login page.
- `/dashboard`: User dashboard (protected route).
- `/logout`: User logout route.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

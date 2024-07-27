# CipherMate - AES Encryption/Decryption

CipherMate is a web application that provides AES encryption and decryption functionality. Users can encrypt or decrypt text using AES-256 encryption via a simple web interface.

## Features

- AES-256 encryption and decryption.
- Clean, dark-themed UI with a video background.
- Form validation with flash messages for user feedback.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/AmishaSharma12002/cipherMate.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd ciphermate
    ```

3. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

6. **Run the application:**

    ```bash
    python app.py
    ```

    Open your web browser and navigate to `http://127.0.0.1:5000` to access the application.

## Requirements

- Python 3.8 or higher
- Flask
- Cryptography
- pymatrix-rain (for optional matrix effect, not used in the current version)

## Project Structure

- `app.py`: Main Flask application file.
- `templates/`: Directory containing HTML templates.
- `static/`: Directory for static files (CSS, video, etc.).
- `requirements.txt`: List of Python dependencies.
- `README.md`: Project documentation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

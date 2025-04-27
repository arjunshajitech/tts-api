# Voice Cloning API

This project provides an API for voice cloning using text and voice input files. It leverages a deep learning model for text-to-speech (TTS) synthesis to generate cloned voice from the provided text and voice samples.

## Prerequisites

Before getting started, make sure you have the following installed:

- Python >= 3.9, < 3.12..
- A GPU with CUDA (version > 2) support for optimal performance.
- CUDA-enabled PyTorch installation.
- The required Python packages (listed in `requirements.txt`).

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository** or download the project files to your local machine.

2. **Navigate to the project directory** where the `requirements.txt` is located.

3. **Install the required dependencies** by running:

    ```bash
    pip install -r requirements.txt
    ```

4. **Start the Flask app** on port 8888 by running:

    ```bash
    flask --app main.py run --port 8888
    ```

    The application will start running at `http://127.0.0.1:8888`.

## API Endpoints

### 1. Health Check Endpoint

```bash
curl --location 'http://127.0.0.1:8888'
```

### 2. Voice Cloning


```bash
curl --location 'http://127.0.0.1:8888/tts/voice-cloning' \
  --form 'text=@"/home/arjun/Desktop/tts-api/text/test.txt"' \
  --form 'voice=@"/home/arjun/Desktop/tts-api/audio/test.wav"'
```

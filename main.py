from flask import Flask, jsonify, request
import os
import torch
from TTS.api import TTS
import torch.serialization
from TTS.tts.configs.xtts_config import XttsConfig

app = Flask(__name__)

torch.serialization.add_safe_globals([XttsConfig])

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Device: {device}")

model_path = "tts_models/multilingual/multi-dataset/xtts_v2"
tts = None
try:
    tts = TTS(model_path).to(device)
    print("TTS model successfully loaded.")
except Exception as e:
    print(f"Error loading model: {e}")

# API route for hello world
@app.route("/")
def hello_world():
    return jsonify({"message": "Hello, World!"})

# API route for uploading text and voice files
@app.route("/tts/voice-cloning", methods=["POST"])
def upload_files():
    if 'text' not in request.files or 'voice' not in request.files:
        return jsonify({"error": "Text and voice files are required"}), 400

    text_file = request.files['text']
    voice_file = request.files['voice']
    
    # Validate file types
    if not text_file.filename.endswith('.txt'):
        return jsonify({"error": "Text file must be .txt"}), 400
    if not voice_file.filename.endswith(('.mp3', '.wav')):
        return jsonify({"error": "Voice file must be .mp3 or .wav"}), 400
    
    # Save files
    upload_folder = 'tts'
    os.makedirs(upload_folder, exist_ok=True)
    output_folder = 'output'
    os.makedirs(output_folder, exist_ok=True)
    
    text_path = os.path.join(upload_folder, text_file.filename)
    voice_path = os.path.join(upload_folder, voice_file.filename)
    
    text_file.save(text_path)
    voice_file.save(voice_path)
    
    try:
        with open(text_path, 'r') as file:
            text = file.read().strip()
        
        if tts is not None:
            print(f"TTS Voice cloning started...")
            output_path = os.path.join("output", "output.wav")
            tts.tts_to_file(text=text, speaker_wav=voice_path, language="en", file_path=output_path)
            print(f"Completed: {output_path}")
            return jsonify({
                "message": "Files uploaded and processed successfully",
                "text_file": text_file.filename,
                "voice_file": voice_file.filename,
                "output_audio": output_path
            })
        else:
            return jsonify({"error": "TTS model failed to load"}), 500

    except Exception as e:
        return jsonify({"error": f"Error processing text or TTS: {e}"}), 500

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify({"message": "Hello, World!"})

@app.route("/tts/voice-cloning", methods=["POST"])
def upload_files():
    print(f"request.files: {request.files}")
    if 'text' not in request.files or 'voice' not in request.files:
        return jsonify({"error": "Text and voice files are required"}), 400
    
    text_file = request.files['text']
    voice_file = request.files['voice']
    
    # Validate file types
    if not text_file.filename.endswith('.txt'):
        return jsonify({"error": "Text file must be .txt"}), 400
    if not voice_file.filename.endswith(('.mp3', '.wav')):
        return jsonify({"error": "Voice file must be .mp3 or .wav"}), 400
    
    # Save files (in a real application, you'd want to secure this)
    upload_folder = 'tts'
    os.makedirs(upload_folder, exist_ok=True)
    
    text_path = os.path.join(upload_folder, text_file.filename)
    voice_path = os.path.join(upload_folder, voice_file.filename)
    
    text_file.save(text_path)
    voice_file.save(voice_path)
    
    return jsonify({
        "message": "Files uploaded successfully",
        "text_file": text_file.filename,
        "voice_file": voice_file.filename
    })

if __name__ == "__main__":
    app.run(debug=True)
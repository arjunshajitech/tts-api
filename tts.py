import torch
from TTS.api import TTS
# import torch.serialization
# from TTS.tts.configs.xtts_config import XttsConfig

# Add the safe global for XttsConfig
# torch.serialization.add_safe_globals([XttsConfig])

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Device: {device}")

# List available TTS models
print(TTS().list_models())

# Init TTS (Using 'weights_only=False' to bypass the pickle issue)
model_path = "tts_models/multilingual/multi-dataset/xtts_v2"

# Try loading the TTS model with the safe global addition
tts = None  # Initialize tts variable
try:
    tts = TTS(model_path).to(device)  # Attempt to load the model
    print("TTS model successfully loaded.")
except Exception as e:
    print(f"Error loading model: {e}")

# Check if the tts object is defined before proceeding
if tts is not None:
    # Run TTS
    try:
        tts.tts_to_file(text="Hello world!", speaker_wav="audio/test.wav", language="en", file_path="output.wav")
        print("Audio file generated: output.wav")
    except Exception as e:
        print(f"Error during TTS: {e}")
else:
    print("Skipping TTS generation as the model failed to load.")
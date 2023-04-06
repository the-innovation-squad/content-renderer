import os
from voice import generate_voice_recording

if __name__ == "__main__":
    api_key = os.environ["ELEVEN_LABS_API_KEY"]
    input_script = "Hello, this is a test script for the Eleven Labs API."
    output_file = "output.mp3"

    generate_voice_recording(api_key, input_script, output_file)
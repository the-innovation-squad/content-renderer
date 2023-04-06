import os
import requests
import json

def generate_voice_recording(api_key, input_script, output_file):
    url = "https://api.elevenlabs.io/v1/synthesize"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "text": input_script,
        "voice": "en-US-Wavenet-A",  # Replace with the desired voice
        "format": "mp3"
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        with open(output_file, 'wb') as f:
            f.write(response.content)
        print(f"Voice recording saved as {output_file}")
    else:
        print(f"Error: {response.status_code}, {response.text}")

if __name__ == "__main__":
    api_key = os.environ["ELEVEN_LABS_API_KEY"]
    input_script = "Hello, this is a test script for the Eleven Labs API."
    output_file = "output.mp3"

    generate_voice_recording(api_key, input_script, output_file)
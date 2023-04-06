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
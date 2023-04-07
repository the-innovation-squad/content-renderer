import requests
from config import Config
cfg = Config()

def generate_voice_recording(input_script):
    tts_headers = {
        "Content-Type": "application/json",
        "xi-api-key": cfg.elevenlabs_api_key
    }

    tts_url = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}".format(
        voice_id="ErXwobaYiN019PkySvjV")
    formatted_message = {"text": input_script}
    response = requests.post(
        tts_url, headers=tts_headers, json=formatted_message)

    output_file = "output/speech.mpeg"
    if response.status_code == 200:
        with open(output_file, "wb") as f:
            f.write(response.content)
        return output_file
    else:
        print("Request failed with status code:", response.status_code)
        print("Response content:", response.content)
        return False
    
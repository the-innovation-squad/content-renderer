import requests

def generate_voice_recording(api_key, input_script, output_file):
    tts_headers = {
        "Content-Type": "application/json",
        "xi-api-key": api_key
    }

    tts_url = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}".format(
        voice_id="ErXwobaYiN019PkySvjV")
    formatted_message = {"text": input_script}
    response = requests.post(
        tts_url, headers=tts_headers, json=formatted_message)

    if response.status_code == 200:
        with open("output/speech.mpeg", "wb") as f:
            f.write(response.content)
        return True
    else:
        print("Request failed with status code:", response.status_code)
        print("Response content:", response.content)
        return False
    
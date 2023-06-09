import requests
from config import config

def narrate(input_script, output_dir, settings):
    voice_id = settings.get("voice_id", "TxGEqnHWrfWFTfGW9XjX")

    tts_headers = {
        "Content-Type": "application/json",
        "xi-api-key": config["ELEVENLABS_API_KEY"]
    }
    tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    formatted_message = {"text": input_script}
    response = requests.post(
        tts_url, headers=tts_headers, json=formatted_message
    )

    if response.status_code == 200:
        output_path = output_dir + "/narration.mpeg"
        with open(output_path, "wb") as f:
            f.write(response.content)
        return output_path
    else:
        print("Request failed with status code:", response.status_code)
        print("Response content:", response.content)
        raise Exception("Eleven Labs TTS Generation Failed: " + response.content)
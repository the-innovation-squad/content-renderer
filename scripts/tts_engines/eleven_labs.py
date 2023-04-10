import requests
from config import Config
cfg = Config()

def narrate(input_script, output_dir, settings):
    voice_id = settings.get("voice_id", "TxGEqnHWrfWFTfGW9XjX")

    tts_headers = {
        "Content-Type": "application/json",
        "xi-api-key": cfg.elevenlabs_api_key
    }
    tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    # TODO: fix issue where we seem to need to clip off script at 333 characters
    formatted_message = {"text": input_script[:333]}
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
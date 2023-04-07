import requests
import shutil
from google.cloud import texttospeech
from config import Config
cfg = Config()

def upscaled_narration(input_script, output_path):
    output_path = output_path + "/narration.mpeg"

    if (cfg.debug):
        print("In DEBUG mode, skipping voice recording generation")
        source_file = "lib/voice-sample.mpeg"
        destination_file = output_path
        shutil.copy2(source_file, destination_file)
        return "lib/voice-sample.mpeg"

    tts_headers = {
        "Content-Type": "application/json",
        "xi-api-key": cfg.elevenlabs_api_key
    }

    tts_url = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}".format(
        voice_id="ErXwobaYiN019PkySvjV")
    # TODO: fix issue where we clip off script at 333 characters
    formatted_message = {"text": input_script[:333]}
    response = requests.post(
        tts_url, headers=tts_headers, json=formatted_message)

    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        return output_path
    else:
        # TODO: tidy this error handling, why return a boolean?
        print("Request failed with status code:", response.status_code)
        print("Response content:", response.content)
        return False

def create_narration(input_script, output_path):
    if(cfg.upscale):
        return upscaled_narration(input_script, output_path)
    
    output_path = output_path + "/narration.mp3"

    # Google Cloud TTS
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=input_script)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-UK", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open(output_path, "wb") as out:
        out.write(response.audio_content)

    return output_path
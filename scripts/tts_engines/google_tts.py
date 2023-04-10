from google.cloud import texttospeech

def narrate(input_script, output_dir, settings):
    language_code = settings.get("language_code", "en-UK")
    ssml_gender_string = settings.get("ssml_gender", "NEUTRAL")
    ssml_gender = texttospeech.SsmlVoiceGender[ssml_gender_string]

    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=input_script)
    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code,
        ssml_gender=ssml_gender
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    output_path = output_dir + "/narration.mp3"
    with open(output_path, "wb") as out:
        out.write(response.audio_content)

    return output_path
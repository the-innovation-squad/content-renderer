from google.cloud import texttospeech

def narrate(input_script, output_dir):
    output_path = output_dir + "/narration.mp3"

    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=input_script)

    voice = texttospeech.VoiceSelectionParams(
        # TODO: extract below settings and expose in script yaml
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
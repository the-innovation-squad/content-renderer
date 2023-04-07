import shutil
from config import Config
cfg = Config()
from tts_engines.google_tts import narrate as narrate_google
from tts_engines.eleven_labs import narrate as narrate_eleven

def create_narration(input_script, options, output_path):
    engine = options["engine"] or "google"
    if engine == "google":
        return narrate_google(input_script, output_path)
    elif engine == "eleven":
        return narrate_eleven(input_script, output_path)
    else:
        raise Exception("Unknown engine: " + engine)
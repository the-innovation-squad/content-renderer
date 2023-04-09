from tts_engines.google_tts import narrate as narrate_google
from tts_engines.eleven_labs import narrate as narrate_eleven
import shutil
from config import Config
cfg = Config()

def create_narration(input_script, options, output_dir):

    if cfg.debug:
        output_path = output_dir + "/narration.mpeg"
        shutil.copy("lib/voice-sample.mpeg", output_path)


    engine = options["engine"]
    if engine == "google":
        return narrate_google(input_script, output_dir)
    elif engine == "eleven":
        return narrate_eleven(input_script, output_dir)
    else:
        raise Exception("Unknown engine: " + engine)
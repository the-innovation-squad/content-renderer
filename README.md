# Video Generator
For a given script, this tool generates a video with the script being read by an AI generated voice.

## Setup
Copy the .env.sample file, rename to .env and fill in the values.
```bash
pip3 install -r requirements.txt
```

## Running
```bash
python3 scripts/main.py
```

### Debug Mode
To skip the audio generation and use a pre-generated audio file, pass the `--debug` (`-d`) flag. This will save you some credits with Eleven Labs.
```bash
python3 scripts/main.py -d
```
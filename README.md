# 🎥 Content Renderer

This tool is designed for rendering videos with a given script and corresponding video clips. It combines the script being read by an AI-generated voice with the provided video clips to create a final video. Please note that this application does not source content or footage; it only renders videos based on the input provided. The content and footage should be prepared separately and provided through the input YAML file.

The project uses the Eleven Labs API to generate the voice narration and MoviePy for video editing.

## 📜 Example Script
Here is a simple example script that can be passed as an input to the app:
```yaml
title: Simple Video Example
watermark: "https://i.imgur.com/NbzMg2q.png" # Optional
captions: True # Optional
timeline:
  - content: "Welcome to our video! This is the first scene with an AI-generated voice."
    clip: "https://www.pexels.com/download/video/6394054/"
  - content: "Now, we're moving to the second scene. Enjoy the visuals!"
    engine: "eleven" # One of ["eleven", "google"]. Default is "google"
    clip: "https://www.pexels.com/download/video/2034291/"
  - content: "That's it for our video. Thanks for watching and stay tuned for more content!"
    clip: "https://www.pexels.com/download/video/3150358/?fps=25.0&h=1080&w=2048"
```
https://user-images.githubusercontent.com/2746248/230598446-d7470b44-a7a5-4cac-b885-b1a41f5ef272.mp4


## ⚙️ Setup and Installation

1. Clone the repository to your local machine.

2. Copy the `.env.sample` file, rename it to `.env`, and fill in the values:
	```bash
	cp .env.sample .env
	```

3. Install the required Python packages:
	```bash
	pip3 install -r requirements.txt
	```

4. If you are on macOS, you may need to install the ffmpeg and imagemagick libraries:
	_If you don't have Homebrew installed, you can follow the installation instructions on their website: https://brew.sh/._
	```bash
	brew install ffmpeg # required for MoviePy to work
	brew install imagemagick # required for MoviePy to support captions
	```

### Environment Variables
- `ELEVEN_LABS_API_KEY`: API key for the Eleven Labs API. You can get one by signing up for a free account at https://eleven-labs.com/
- `GOOGLE_APPLICATION_CREDENTIALS`: Path to the Google Cloud Platform service account credentials JSON file. You can get one by following the instructions at https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries#client-libraries-install-python

## 🚀 Running the App

1. To run the app, simply execute the following command:
	```bash
	python3 scripts/main.py
	```
	This will create a video based on the input script and stock video clips provided in the input/video_script.yml file. The final video will be saved in the output directory.

## 🔧 Available Arguments

| Short | Long      | Description                                | Type           |
|-------|-----------|--------------------------------------------|----------------|
| `-d`  | `--debug` | Enable debug mode, and skip tts generation | Flag (boolean) |

### Usage

To run the script with command-line arguments, use the following format:

```bash
python scripts/main.py [-d]
```

## 📖 How the App Works
The app works in the following steps:

1. Read the input script and video clips from the input/video_script.yml file.

2. Generate the voice narration using the Eleven Labs API or use a pre-generated audio file in debug mode.

3. Create video segments for each timeline item in the input script, combining the video clips with the generated voice narration.

4. Concatenate the video segments together to produce the final video.

5. Save the final video in the output directory.


Feel free to modify and enhance the README to better suit your project's needs.

# Video Generator 🎥

_Please enjoy our GPT-4 written README! 🤖_

This tool is designed for rendering videos with a given script and corresponding video clips. It combines the script being read by an AI-generated voice with the provided video clips to create a final video. Please note that this application does not source content or footage; it only renders videos based on the input provided. The content and footage should be prepared separately and provided through the input YAML file.

The project uses the Eleven Labs API to generate the voice narration and MoviePy for video editing.

## 📜 Example Script
Here is a simple example script that can be passed as an input to the app:
```yaml
title: Simple Video Example
timeline:
  - content: "Welcome to our video! This is the first scene with an AI-generated voice."
    clip: "https://shorturl.at/oqJN3"
  - content: "Now, we're moving to the second scene. Enjoy the visuals!"
    clip: "https://shorturl.at/kmBQ6"
  - content: "That's it for our video. Thanks for watching and stay tuned for more content!"
    clip: "https://shorturl.at/bpxX9"
```
https://user-images.githubusercontent.com/2746248/230537798-f37819a3-c6df-4a34-96e8-d0e3b7b67a94.mp4

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

## 🚀 Running the App

1. To run the app, simply execute the following command:
	```bash
	python3 scripts/main.py
	```
	This will create a video based on the input script and stock video clips provided in the input/video_script.yml file. The final video will be saved in the output directory.

## 🔰 Instructions for Beginners

If you are new to Python and command-line applications, follow these steps:

Install Python 3 from the [official Python website](https://www.python.org/downloads/).

Open a terminal (Command Prompt on Windows, Terminal on macOS/Linux) and navigate to the project directory using the cd command.

Follow the setup and installation instructions above.

Run the app using the command provided in the "Running the App" section.

## 🔧 Available Arguments

### Debug Mode
To skip the audio generation and use a pre-generated audio file, pass the --debug (-d) flag. This will save you some credits with Eleven Labs.

```bash
python3 scripts/main.py -d
```

## 📖 How the App Works
The app works in the following steps:

1. Read the input script and video clips from the input/video_script.yml file.

2. Generate the voice narration using the Eleven Labs API or use a pre-generated audio file in debug mode.

3. Create video segments for each timeline item in the input script, combining the video clips with the generated voice narration.

4. Concatenate the video segments together to produce the final video.

5. Save the final video in the output directory.


Feel free to modify and enhance the README to better suit your project's needs.

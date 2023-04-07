from moviepy.editor import *
import requests
import os

def add_watermark(input_video_path, watermark_url, output_video_path):
    watermark_path = download_img(watermark_url)
    # Load the video clip
    clip = VideoFileClip(input_video_path)

    # Load the watermark image
    watermark = ImageClip(watermark_path)

    watermark = watermark.set_duration(clip.duration).resize(width=100)

    # Define the position of the watermark
    position = (clip.w - watermark.w - 10, clip.h - watermark.h - 10)

    # Add the watermark to the video clip
    video_with_watermark = CompositeVideoClip(
        [clip, watermark.set_position(position)])

    # Add the original audio to the final output
    video_with_watermark = video_with_watermark.set_audio(clip.audio)

    # Write the video clip to a file
    video_with_watermark.write_videofile(output_video_path, codec="libx264", audio_codec="aac")

def download_img(url):
    response = requests.get(url)

    if response.status_code == 200:
        filename = "output/watermark.png"
        with open(filename, "wb") as file:
            file.write(response.content)
        return os.path.abspath(filename)
    else:
        print(f"Failed to download the image, status code: {response.status_code}")
        raise Exception(f"Failed to download the image, status code: {response.status_code}")

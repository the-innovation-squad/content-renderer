from moviepy.editor import ImageClip, CompositeVideoClip
import requests
import os

def add_watermark(input_video, watermark_url):
    watermark_path = download_img(watermark_url)

    # Load the watermark image
    watermark = ImageClip(watermark_path)

    watermark = watermark.set_duration(input_video.duration).resize(width=100)

    # Define the position of the watermark
    position = (
        input_video.w - watermark.w - 10,
        input_video.h - watermark.h - 10
    )

    # Add the watermark to the video clip
    video_with_watermark = CompositeVideoClip(
        [input_video, watermark.set_position(position)]
    )
    return video_with_watermark

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

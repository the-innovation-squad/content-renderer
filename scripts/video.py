import requests
import subprocess
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
from video_tools.watermark import add_watermark
from video_tools.captions import add_captions
from video_tools.resize import resize_and_crop

def download_video(video_url, ouput_path):
    response = requests.get(video_url, stream=True)
    if response.status_code == 200:
        with open(ouput_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    else:
        print(f"Request failed with status code: {response.status_code}")
        raise Exception(f"Request failed with status code: {response.status_code}")

def create_segment(audio_path, video_url, content, video_options, output_dir):
    output_path = output_dir + "/video.mp4"
    download_video(video_url, output_path)

    video_clip = VideoFileClip(output_path)
    audio = AudioFileClip(audio_path)

    # Calculate the number of loops needed for the video to match the audio duration
    num_loops = int(audio.duration // video_clip.duration) + 1

    # Create a list of video clips to concatenate
    video_clips = [video_clip] * num_loops

    # Concatenate the video clips to create a looped video
    looped_video_clip = concatenate_videoclips(video_clips)

    # Set the audio of the looped video to the loaded audio file
    final_video = looped_video_clip.set_audio(audio)

    # Trim the video to match the audio duration
    final_video = final_video.set_duration(audio.duration)
    # Cut the last 1/20th of a second to avoid audio artifacts
    final_video = final_video.subclip(0, final_video.duration - 0.05)

    final_video = resize_and_crop(final_video, video_options["resolution"])
    final_video = final_video.set_fps(24)

    if video_options["watermark_url"]:
        final_video = add_watermark(final_video, video_options["watermark_url"])
    if video_options["captions"]:
        final_video = add_captions(final_video, content)

    output_path_processed = output_path.replace(".mp4", "_processed.mp4")
    final_video.write_videofile(output_path_processed, codec="libx264", audio_codec="aac")
    return output_path_processed

def concatenate_segments(segment_paths, output_path):
    # Here we use ffmpeg command line directly, because moviepy's concatenate_videoclips method creates audio artifacts when combining clips
    # Be wary, errors within this block do not always display clearly
    relative_segment_paths = [path.replace("output/", "") for path in segment_paths]
    with open('output/clip_paths.txt', 'w') as file:
        for path in relative_segment_paths:
            file.write(f"file {path}\n")
    ffmpeg_command = [
        "ffmpeg",
        "-f", "concat",
        "-safe", "0",
        "-i", "output/clip_paths.txt",
        "-c", "copy",
        output_path
    ]
    result = subprocess.run(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        raise Exception(f"Video concatenation failed. Error: {result.stderr}")
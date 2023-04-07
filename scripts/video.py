from moviepy.editor import *
import requests

def download_video(video_url, ouput_path):
    response = requests.get(video_url, stream=True)
    # Ensure the request is successful before proceeding
    if response.status_code == 200:
        with open(ouput_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    else:
        # TODO: throw error here or use placeholder clip
        print(f"Request failed with status code: {response.status_code}")

def create_segment(audio_path, video_url, output_path):
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
    video_with_audio = looped_video_clip.set_audio(audio)

    # Trim the video to match the audio duration
    final_video = video_with_audio.set_duration(audio.duration)

    output_path_processed = output_path.replace(".mp4", "_processed.mp4")
    final_video.write_videofile(output_path_processed, codec="libx264", audio_codec="aac")
    return output_path_processed

def preprocess_video_clip(video_path, target_resolution, target_fps):
    clip = VideoFileClip(video_path)
    resized_clip = clip.resize(target_resolution).set_fps(target_fps)
    return resized_clip

def concatenate_segments(segment_paths, output_path):
    target_resolution = (1920, 1080) # Adjust this to your desired resolution
    target_fps = 30 # Adjust this to your desired frame rate

    processed_clips = [preprocess_video_clip(clip_path, target_resolution, target_fps) for clip_path in segment_paths]
    final_clip = concatenate_videoclips(processed_clips)
    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
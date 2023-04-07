from moviepy.editor import *

def get_shutterstock_video(video_url):
    # get video from Shutterstock using url
    return "input/stock.mp4"

def create_segment(audio_path, video_url, ouput_path):
    video_path = get_shutterstock_video(video_url)

    output_video = ouput_path
    watermark = "logo.png"

    video_clip = VideoFileClip(video_path)
    #watermark_clip = ImageClip(watermark, duration=video_clip.duration)

    audio = AudioFileClip(audio_path)

    # Set the audio of the video to the loaded audio file
    video_with_audio = video_clip.set_audio(audio)

    # Position the watermark at the bottom-right corner
    watermark_pos = ("right", "bottom")

    #final_clip = CompositeVideoClip([video_with_audio, watermark_clip.set_position(watermark_pos)])
    video_with_audio.write_videofile(output_video, codec="libx264", audio_codec="aac")

def concatenate_segments(segment_paths):
    # Concatenate the video segments together
    final_clip = concatenate_videoclips([VideoFileClip(m).subclip(0, 10) for m in segment_paths])
    final_clip.write_videofile("output/final.mp4", codec="libx264", audio_codec="aac")
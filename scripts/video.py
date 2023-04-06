from moviepy.editor import *

input_video = "input/input.mp4"
output_video = "output/output.mp4"
watermark = "logo.png"

video_clip = VideoFileClip(input_video).subclip(50,60)
watermark_clip = ImageClip(watermark, duration=video_clip.duration)

audio = AudioFileClip("output/speech.mpeg")

# Set the audio of the video to the loaded audio file
video_with_audio = video_clip.set_audio(audio)

# Position the watermark at the bottom-right corner
watermark_pos = ("right", "bottom")

final_clip = CompositeVideoClip([video_with_audio, watermark_clip.set_position(watermark_pos)])
final_clip.write_videofile(output_video, codec="libx264", audio_codec="aac")

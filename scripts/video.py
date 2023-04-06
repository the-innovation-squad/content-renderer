from moviepy.editor import *

input_video = "video.mp4"
output_video = "watermarked_output.mp4"
watermark = "logo.png"

video_clip = VideoFileClip(input_video).subclip(50,60)
watermark_clip = ImageClip(watermark, duration=video_clip.duration)

# Position the watermark at the bottom-right corner
watermark_pos = ("right", "bottom")

final_clip = CompositeVideoClip([video_clip, watermark_clip.set_position(watermark_pos)])
final_clip.write_videofile(output_video)

from moviepy.editor import *

def add_captions(video, subtitle_text):
    captions = TextClip(subtitle_text, fontsize=48, color="white", font="Comic-Sans-MS-Bold")
    captions = captions.set_position(
        ("center", video.size[1]*0.75)
    ).set_duration(video.duration)

    video_with_captions = CompositeVideoClip([video, captions])
    return video_with_captions
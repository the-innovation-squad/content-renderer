from moviepy.editor import *

def add_captions(video, content, is_captioning_enabled):
    if not is_captioning_enabled:
        return video

    subtitle_text = content
    subtitle = TextClip(subtitle_text, fontsize=48, color="white", font="Comic-Sans-MS-Bold")
    subtitle = subtitle.set_position(
        ("center",  video.size[1]*0.75)).set_duration(video.duration)

    video_with_sub = CompositeVideoClip([video, subtitle])
    return video_with_sub

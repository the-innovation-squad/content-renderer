import textwrap
from moviepy.editor import TextClip, CompositeVideoClip, ColorClip

def get_wrap_width(video_width, char_width=20):
    return video_width // char_width

def add_captions(video, caption_text):
    # Calculate the wrap width based on the video width
    wrap_width = get_wrap_width(video.w)

    # Create the TextClip with proper wrapping, font, and fontsize
    wrapped_caption_text = "\n".join(textwrap.wrap(caption_text, width=wrap_width))
    subtitle = TextClip(wrapped_caption_text, fontsize=24, color="white", font="Arial", size=video.size)

    # Create a semi-transparent background for the subtitle text to make it more readable
    subtitle_background = ColorClip(size=(video.w, subtitle.h), color=(0, 0, 0), duration=video.duration).set_opacity(0.6)

    # Set the position of the subtitle and background (bottom-center)
    subtitle_position = ("center", video.h - subtitle.h - 10)
    subtitle = subtitle.set_position(subtitle_position).set_duration(video.duration)
    subtitle_background = subtitle_background.set_position(subtitle_position).set_duration(video.duration)

    # Create a CompositeVideoClip with the original video, subtitle background, and subtitle text
    video_with_captions = CompositeVideoClip([video, subtitle_background, subtitle])

    return video_with_captions
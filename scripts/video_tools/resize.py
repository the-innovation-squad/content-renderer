def resize_and_crop(video_clip, resolution_string):
    resolution_array = [int(num) for num in resolution_string.split(', ')]
    output_width = resolution_array[0]
    output_height = resolution_array[1]

    input_width, input_height = video_clip.size
    input_aspect_ratio = input_width / input_height
    output_aspect_ratio = output_width / output_height

    if input_aspect_ratio > output_aspect_ratio:
        # Resize based on height
        new_height = output_height
        new_width = int(output_height * input_aspect_ratio)
    else:
        # Resize based on width
        new_width = output_width
        new_height = int(output_width / input_aspect_ratio)

    # Resize the video while preserving the aspect ratio
    resized_clip = video_clip.resize(newsize=(new_width, new_height))

    # Crop the video to the desired output resolution
    cropped_clip = resized_clip.crop(
        x_center=resized_clip.w / 2,
        y_center=resized_clip.h / 2,
        width=output_width,
        height=output_height,
    )

    return cropped_clip
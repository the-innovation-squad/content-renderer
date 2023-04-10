def set_orientation(clip):
    # Load the video clip
    # Get the current aspect ratio of the video
    width, height = clip.size
    print('SIZES', width, height)
    aspect_ratio = float(width) / float(height)

    # Calculate the dimensions of the crop area
    if aspect_ratio > 9/16:
        # Crop horizontally
        new_width = int(height * 9/16)
        x_offset = int((width - new_width) / 2)
        width=new_width
        y_offset = 0
    else:
        # Crop vertically
        new_height = int(width * 16/9)
        x_offset = 0
        y_offset = int((height - new_height) / 2)
        height=new_height

    # Apply the crop
    clip = clip.crop(x1=x_offset, y1=y_offset, x2=x_offset +
                     width, y2=y_offset+height)

    # Save the cropped video to a file
    return clip

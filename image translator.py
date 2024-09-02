import os
from PIL import Image, ImageDraw, ImageFont

def text_to_image(text, output_image_path, font_path=None, font_size=20, image_size=(500, 300), text_color=(0, 0, 0), bg_color=(255, 255, 255)):
    """
    Converts the given text into an image and saves it.

    :param text: The text to convert into an image.
    :param output_image_path: The path to save the output image.
    :param font_path: The path to a .ttf font file. Defaults to None, which uses the default font.
    :param font_size: The size of the font.
    :param image_size: A tuple specifying the width and height of the image.
    :param text_color: A tuple specifying the color of the text (RGB format).
    :param bg_color: A tuple specifying the background color of the image (RGB format).
    """
    # Create a blank image with the specified background color
    image = Image.new("RGB", image_size, color=bg_color)
    draw = ImageDraw.Draw(image)

    # Load the specified font, or use the default font
    if font_path:
        font = ImageFont.truetype(font_path, font_size)
    else:
        font = ImageFont.load_default()

    # Function to wrap text
    def wrap_text(text, font, max_width):
        lines = []
        words = text.split()
        line = ""
        for word in words:
            test_line = f"{line} {word}".strip()
            width, _ = draw.textbbox((0, 0, 0, 0), test_line, font=font)[2:]
            if width <= max_width:
                line = test_line
            else:
                lines.append(line)
                line = word
        if line:
            lines.append(line)
        return lines

    # Wrap text if needed
    max_width = image_size[0] - 20  # Margin
    wrapped_text = wrap_text(text, font, max_width)

    # Calculate total text height
    total_text_height = sum(draw.textbbox((0, 0, 0, 0), line, font=font)[3] for line in wrapped_text)
    y = (image_size[1] - total_text_height) / 2

    # Draw each line of text on the image
    for line in wrapped_text:
        text_width, text_height = draw.textbbox((0, 0, 0, 0), line, font=font)[2:]
        position = ((image_size[0] - text_width) / 2, y)
        draw.text(position, line, fill=text_color, font=font)
        y += text_height

    # Ensure the directory exists
    directory = os.path.dirname(output_image_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Save the image to the specified path
    image.save(output_image_path)
    print(f"Image saved as {output_image_path}")

if __name__ == "__main__":
    # Text to convert into an image
    text = input("Enter Text: ")  # Replace with your desired text

    # Path to save the output image
    output_image_path = "ocr_practice/output_image.png"  # Make sure to specify the file extension

    # Optional: Path to a .ttf font file (use a font that supports the language you are using)
    font_path = None  # Replace with the path to your .ttf font file, or leave as None to use the default font

    # Convert the text to an image
    text_to_image(text, output_image_path, font_path=font_path)

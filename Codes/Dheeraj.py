from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_glow_text(text, font_path, font_size, glow_radius, text_color, glow_color, outfile):
    # Create blank image with extra room for the glow
    w, h = (600, 200)
    image = Image.new("RGBA", (w, h), (0, 0, 0, 0))

    # Load font
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()

    # Draw glowing text on a separate layer
    glow_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow_layer)
    text_width, text_height = glow_draw.textsize(text, font=font)
    xy = ((w - text_width) // 2, (h - text_height) // 2)

    # Draw thicker text for glow
    for offset in range(-glow_radius, glow_radius + 1, 2):
        for yoffset in range(-glow_radius, glow_radius + 1, 2):
            glow_draw.text((xy[0] + offset, xy[1] + yoffset), text, font=font, fill=glow_color)

    # Blur the layer for the glow
    blurred_glow = glow_layer.filter(ImageFilter.GaussianBlur(radius=glow_radius // 2))

    # Composite glow & draw main text
    final_img = Image.alpha_composite(image, blurred_glow)
    draw = ImageDraw.Draw(final_img)
    draw.text(xy, text, font=font, fill=text_color)

    # Save as PNG with alpha
    final_img.save(outfile)

if __name__ == "__main__":
    create_glow_text(
        text="Dheeraj",
        font_path="arial.ttf",    # Or a path to a .ttf on your system
        font_size=72,
        glow_radius=10,
        text_color=(255, 255, 255, 255),
        glow_color=(0, 255, 255, 200),
        outfile="Dheeraj_glow_logo.png"
    )

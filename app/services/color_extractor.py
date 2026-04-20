from PIL import Image


def extract_top_colors(image_path, k=10):
    image = Image.open(image_path)

    # Convert to palette mode with k colors
    image = image.convert('P', palette=Image.ADAPTIVE, colors=k)

    # Convert back to RGB
    image = image.convert('RGB')

    colors = image.getcolors(200*200)

    # Sort by frequency
    colors.sort(reverse=True)

    top_colors = [color[1] for color in colors[:k]]

    return top_colors
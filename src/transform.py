from PIL import Image, ImageOps
import io
import pillow_heif

pillow_heif.register_heif_opener()

class ImageTransformer:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def transform(self, path):
        canvas = Image.new("RGB", (self.width, self.height), (0, 0, 0))
        img = Image.open(path)
        # Correct orientation using EXIF data if present
        img = ImageOps.exif_transpose(img)
        img = img.convert("RGB")

        # Fit image to canvas, maintaining aspect ratio
        img = ImageOps.contain(img, (self.width, self.height))
        # Center the image on the canvas
        x = (self.width - img.width) // 2
        y = (self.height - img.height) // 2
        canvas.paste(img, (x, y))
        # Save to JPEG binary
        output = io.BytesIO()
        canvas.save(output, format="JPEG")
        return output.getvalue()

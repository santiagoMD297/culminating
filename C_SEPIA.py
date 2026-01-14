from PIL import Image

class CustomImage:

    def __init__(self, filename: str):
        # Load image
        self.image = Image.open(filename)
        self.pixels = self.image.load()
        self.width, self.height = self.image.size
        self.filename = filename

        # Immediately create and save sepia version
        self.apply_sepia()

    def apply_sepia(self):
        """
        Apply sepia filter to each pixel in the image using the formulas:
        
        tr = 0.393R + 0.769G + 0.189B
        tg = 0.349R + 0.686G + 0.168B
        tb = 0.272R + 0.534G + 0.131B
        """

        for y in range(self.height):
            for x in range(self.width):

                r, g, b = self.pixels[x, y]

                # Calculate new values
                tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                tb = int(0.272 * r + 0.534 * g + 0.131 * b)

                # Clamp values to max 255
                r_new = min(255, tr)
                g_new = min(255, tg)
                b_new = min(255, tb)

                # Set new pixel
                self.pixels[x, y] = (r_new, g_new, b_new)

        # Save the modified image
        self.save_sepia()

    def save_sepia(self):
        """
        Save new sepia image using naming rule:
        eiffeltower.jpg → eiffeltower_sepia.jpg
        """

        # Split filename into name + extension
        base, ext = self.filename.rsplit(".", 1)
        sepia_name = f"{base}_sepia.{ext}"

        # Save
        self.image.save(sepia_name)
        print(f"Saved sepia image as {sepia_name}")


# Example run (you may delete this when submitting)
if __name__ == "__main__":
    CustomImage("eiffeltower.jpg")

# test
import os
from PIL import Image
from sepia import CustomImage

def test_sepia_output_file():
    # Create test image
    test_image = Image.new("RGB", (2, 2), (100, 150, 200))
    test_image.save("testpic.jpg")

    # Apply sepia
    CustomImage("testpic.jpg")

    # Check output file exists
    assert os.path.exists("testpic_sepia.jpg")

def test_pixel_transformation():
    # Load sepia image
    img = Image.open("testpic_sepia.jpg")
    r, g, b = img.load()[0, 0]

    # Expected sepia calculation
    expected_r = min(255, int(0.393*100 + 0.769*150 + 0.189*200))
    expected_g = min(255, int(0.349*100 + 0.686*150 + 0.168*200))
    expected_b = min(255, int(0.272*100 + 0.534*150 + 0.131*200))

    assert (r, g, b) == (expected_r, expected_g, expected_b)
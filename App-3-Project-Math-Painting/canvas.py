import numpy as np
from PIL import Image


class Canvas:

    def __init__(self, height, width, color=[255, 255, 255]):
        self.height = height
        self.width = width
        self.color = color
        self.imagepath = "Canvas1.png"

        # Create a 3d numpy array
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color  # color is an array

    def make(self):
        img = Image.fromarray(self.data, "RGB")
        img.save(self.imagepath)
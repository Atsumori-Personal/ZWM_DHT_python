import numpy as np
from PIL import Image

class Watermark:
    def __init__(self, path: str):
        grey = np.array(Image.open(path).convert('L'))
        self._height, self._width = grey.shape
        self._data = grey > 128
    
    @property
    def height(self):
        return self._height
    
    @property
    def width(self):
        return self._width
    
    @property
    def data(self):
        return self._data
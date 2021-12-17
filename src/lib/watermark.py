import numpy as np
from PIL import Image

class Watermark:
    def __init__(self, path: str):
        grey = np.array(Image.open(path).convert('L'))
        self._h, self._w = grey.shape
        self._data = grey > 128
    
    @property
    def h(self):
        return self._h
    
    @property
    def w(self):
        return self._w
    
    @property
    def data(self):
        return self._data
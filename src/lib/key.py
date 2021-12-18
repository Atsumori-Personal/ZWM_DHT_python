
import numpy as np

class Key:
    def __init__(self, height: int, width: int):
        self._height = height
        self._width = width
        self.data = np.zeros((height, width))
    
    @property
    def height(self):
        return self._height
    
    @property
    def width(self):
        return self._width
    
    def data(self):
        return self.data
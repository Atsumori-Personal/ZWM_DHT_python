
import numpy as np

class Key:
    def __init__(self, height: int, width: int):
        self._h = height
        self._w = width
        self.data = np.zeros((height, width))
    
    @property
    def h(self):
        return self._h
    
    @property
    def w(self):
        return self._w
    
    def data(self):
        return self.data
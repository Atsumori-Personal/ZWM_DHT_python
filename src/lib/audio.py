#%%
import scipy.io.wavfile as wf
import numpy as np
import math
import matplotlib.pyplot as plt

class Audio:
    def __init__(self, path: str):
        self._fs, self._y = wf.read(path)
        dim = self._y.shape
        self._size = dim[0]
        # convert to monaural
        if len(dim) != 1:
            self._y = self._y[:, 0]
    
    @property
    def fs(self):
        return self._fs
    
    @property
    def y(self):
        return self._y

    @property
    def sz(self):
        return self._size
    
    def normalize(self):
        """
        - Common data types[NumPy dtype]
            float32, int32, int16, uint8
        - Reference
            https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.read.html
        """
        y = self._y
        if y.dtype == "float32" or y.dtype == "float64":
            y_max = 1
        elif y.dtype == "int32":
            y_max = np.abs(np.iinfo(np.int32).min)
        elif y.dtype == "int16":
            y_max = np.abs(np.iinfo(np.int16).min)
        elif y.dtype == "uint8":
            y = y + np.iinfo(np.int8).min
            y_max = np.abs(np.iinfo(np.int8).min)
        else:
            raise ValueError("Not supposed data type!")
    
        y_normalized = y / y_max
        y_normalized = y_normalized.astype(np.float32)
        return y_normalized

    def dht(self, y):
        Y = np.fft.fft(y)
        return (Y.real - Y.imag)
    
    def process(self, height: int, width: int):
        """
        M : hight x width (Watermark)
        L : Length of audio signal
        C : Coefficient of DHT
        Q : Number of samples each frame has
        """
        M = height * width
        L = self._size
        C = self.dht(self.normalize())
        Q = math.floor(L / M)

        x = np.zeros(M)
        start = 0
        end = Q - 1

        for i in range(M):
            si = 0
            for j in range(start, end):
                si += abs(C[j])
            start = end
            end = start + Q
            # ti : fractional value of si
            si = str(si).split('.')
            ti = int(si[1])
            xi = np.mod(ti, 2) 
            x[i] = xi
        
        return x.reshape([height, width])
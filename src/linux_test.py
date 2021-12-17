import numpy as np
import matplotlib.pyplot as plt

from lib.watermark import Watermark
from lib.audio import Audio

W = Watermark("image/BN.jpg")

audio = Audio("sound/Thousand Yard Stare.wav")
X = audio.process(W.h, W.w)

K = np.logical_xor(W.data, X)

plt.imshow(K)
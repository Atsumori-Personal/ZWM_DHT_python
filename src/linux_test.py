import numpy as np
import matplotlib.pyplot as plt

from lib.watermark import Watermark
from lib.audio import Audio

"""
Embed
    Generate K by xor(W: watermark, X: audio).
"""
W = Watermark("image/jai-logo-100.jpg")

audio = Audio("sound/Thousand Yard Stare.wav")
X = audio.process(W.height, W.width)

K = Key(W.height, W.width)
K.data = np.logical_xor(W.data, X)

# plt.imshow(K)


"""
Detection
    Generate Watermark and make sure the equality of it with original
    under the assumption that we know the key K.
"""
d_audio = Audio(CURRENT_DIR + "/sound/Thousand Yard Stare.wav")
d_X = d_audio.process(K.height, K.width)

d_W = np.logical_xor(K.data, d_X)

plt.imshow(d_W)
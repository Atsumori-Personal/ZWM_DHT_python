#%%
import numpy as np
import matplotlib.pyplot as plt

"""
Add the path so that it can be used with JupyterNotebook.
"""
import sys, os
from pathlib import Path
CURRENT_DIR = os.path.join(Path().resolve())
sys.path.append(str(CURRENT_DIR) + '/lib')

from watermark import Watermark
from audio import Audio
from key import Key
from myeval import ber

"""
Embed
    Generate K by xor(W: watermark, X: audio).
"""
W = Watermark(CURRENT_DIR + "/image/jai-logo-100.jpg")

audio = Audio(CURRENT_DIR + "/sound/Thousand Yard Stare.wav")
X = audio.process(W.height, W.width)

K = Key(W.height, W.width)
K.data = np.logical_xor(W.data, X)

# plt.imshow(K.data)


"""
Detection
    Generate Watermark and make sure the equality of it with original
    under the assumption that we know the key K.
"""
d_audio = Audio(CURRENT_DIR + "/sound/Thousand Yard Stare.wav")
# d_audio = Audio(CURRENT_DIR + "/sound/Thousand Yard Stare(lpf).wav")
d_X = d_audio.process(K.height, K.width)

d_W = np.logical_xor(K.data, d_X)

print(d_W)
plt.imshow(d_W)

print("BER : " + str(ber(W.data, d_W)))
# %%

import sys
sys.path.insert(1,'dsp-modulo')

import numpy as np
import thinkplot as plt

from thinkdsp import decorate
from thinkdsp import PinkNoise

pendientes = [0.0, 1.5, 2.0]

for pendiente in pendientes:
    senal = PinkNoise(beta=pendiente)
    wave = senal.make_wave(duration=0.5, framerate=22050)
    #wave.write("ruidorosa.wav")

    #wave.plot()
    #decorate(xlabel="tiempo",ylabel="amplitud")
    #plt.show()

    etiqueta = f'pendiente={pendiente}'
    #etiqueta = "pendiente=" + pendiente

    espectro = wave.make_spectrum()
    espectro.plot_power()

loglog = dict(xscale="log",yscale="log")
decorate(xlabel="frecuencia", ylabel="poder", **loglog)
plt.show()
import sys
sys.path.insert(1,'dsp-modulo')

import numpy as np
import thinkplot as plt

from thinkdsp import decorate
from thinkdsp import BrownianNoise

senal = BrownianNoise()
wave = senal.make_wave(duration=0.5, framerate=22050)
#wave.write("ruidoBrowniano.wav")

wave.plot()
decorate(xlabel="Tiempo", ylabel="Amplitud")
plt.show()


espectro = wave.make_spectrum()
espectro.plot_power()
loglog = dict(xscale="log", yscale="log")
decorate(xlabel="frecuencia",ylabel="poder", **loglog)
plt.show()

pendiente = espectro.estimate_slope()
print("pendiente" + str(pendiente.slope))
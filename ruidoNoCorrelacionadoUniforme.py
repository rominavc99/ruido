import sys
sys.path.insert(1,'dsp-modulo')

import numpy as np
import thinkplot as pl

from thinkdsp import decorate
from thinkdsp import UncorrelatedUniformNoise

senal = UncorrelatedUniformNoise()
wave = senal.make_wave(duration=0.5, framerate=22050)
#wave.write("ruidoNoCorrelacionadoUniforme.wav")

segmento = wave.segment(duration=0.05)

segmento.plot()
decorate(xlabel="tiempo", ylabel="amplitud")
pl.show()

espectro = wave.make_spectrum()
espectro.plot_power()
decorate(xlabel="frecuencia", ylabel="power")
pl.show()

espectro_integrado = espectro.make_integrated_spectrum()
espectro_integrado.plot_power()
decorate(xlabel = "frecuencia", ylabel = "poder acumulado")
pl.show()

pendiente = espectro.estimate_slope()
print("pendiente: " + str(pendiente.slope))


# Demodulation Radio Teletype (RTTY) in Python
This is a Python program to demodulate the radio teletype known as FSK modulation.
This is the simplest example, and only the Terminal Unit part of the RTTY is implemented. The rest should be coded according to ITA2, for example.

## Description of the source code

~~~
import wave
import numpy as np
fname='rtty3s.wav' # should be specify the filename.
smp= 8000          # Sampling Rate
FQm= smp/914.0     # Mark Frequency 914Hz
FQs= smp/1086.0    # Space Frequency 1086Hz
wind= 32           # windows size Integer
waveFile = wave.open(fname, 'r')
j=0
for i in range(int(waveFile.getnframes()/wind)):
     buf = waveFile.readframes(wind)
     Im=0;Qm=0;Is=0;Qs=0
     for c in buf:
          Im=Im+((c-128)*np.sin(np.pi*2.0/FQm*j))
          Qm=Qm+((c-128)*np.cos(np.pi*2.0/FQm*j))
          Is=Is+((c-128)*np.sin(np.pi*2.0/FQs*j))
          Qs=Qs+((c-128)*np.cos(np.pi*2.0/FQs*j))
          j = j + 1
     mk = np.sqrt(Im**2 + Qm**2)
     sp = np.sqrt(Is**2 + Qs**2)     
     print(mk,sp,int(mk>sp),sep=",")
waveFile.close()
~~~
## Usage
Please specify an appropriate audio file for the input.
This program assumes 8KHz sampling, mono, 8bit quantization, and no sign.
~~~
python rtty8k.py > rtty.csv
~~~
Demodulation example
![](img/2021-02-01.png)

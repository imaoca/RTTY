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

mq=[];mi=[];sq=[];si=[]
for j in range(waveFile.getnframes()):
      buf = waveFile.readframes(1)
      mq.append((buf[0]-128)*np.sin(np.pi*2.0/FQm*j))
      mi.append((buf[0]-128)*np.cos(np.pi*2.0/FQm*j))
      sq.append((buf[0]-128)*np.sin(np.pi*2.0/FQs*j))
      si.append((buf[0]-128)*np.cos(np.pi*2.0/FQs*j))
      mk = np.sqrt(sum(mq)**2 + sum(mi)**2)
      sp = np.sqrt(sum(sq)**2 + sum(si)**2)     
      print(mk,sp,int(mk>sp),sep=",")
      if j>wind:
            mq.pop(0);mi.pop(0);sq.pop(0);si.pop(0)
waveFile.close()
~~~
## Sample sound file
should be convet to wave format.<p>
https://en.wikipedia.org/wiki/File:RTTY.ogg <p>
it is from wikipedia<p>

## Usage
Please specify an appropriate audio file for the input.
This program assumes 8KHz sampling, mono, 8bit quantization, and no sign.
~~~
python rtty8k.py > rtty.csv
~~~
Demodulation example
![](img/2021-02-01.png)

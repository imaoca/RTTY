import wave
import numpy as np
fname = 'rtty3s.wav'     # should be specify the filename.
waveFile = wave.open(fname, 'r')
buf = waveFile.readframes(-1)
waveFile.close()

Smp = 8000          # Sampling Rate
FQm = Smp/914.0     # Mark Frequency 914Hz
FQs = Smp/1086.0    # Space Frequency 1086Hz
Baud = 176          # Smp/45.45 but shuold be Integer

Im=[];Qm=[];Is=[];Qs=[]
for i in range(0, 8000):
     Im.append((buf[i]-128)*np.sin(np.pi*2.0/FQm*i))
     Qm.append((buf[i]-128)*np.cos(np.pi*2.0/FQm*i))
     Is.append((buf[i]-128)*np.sin(np.pi*2.0/FQs*i))
     Qs.append((buf[i]-128)*np.cos(np.pi*2.0/FQs*i))

for i in range(0, 8000-Baud):
     print (np.sqrt(sum(Im[i:i+Baud])**2 + sum(Qm[i:i+Baud])**2),end=",")
     print (np.sqrt(sum(Is[i:i+Baud])**2 + sum(Qs[i:i+Baud])**2))

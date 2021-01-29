import wave
import numpy as np

fname='rtty3s.wav' # should be specify the filename.
smp= 8000          # Sampling Rate
FQm= smp/914.0     # Mark Frequency 914Hz
FQs= smp/1086.0    # Space Frequency 1086Hz
wind= 176          # wind = smp/45.45 but shuold be Integer

waveFile = wave.open(fname, 'r')
buf = waveFile.readframes(-1)
waveFile.close()

Im=[];Qm=[];Is=[];Qs=[]
for i in range(0, 8000):
     Im.append((buf[i]-128)*np.sin(np.pi*2.0/FQm*i))
     Qm.append((buf[i]-128)*np.cos(np.pi*2.0/FQm*i))
     Is.append((buf[i]-128)*np.sin(np.pi*2.0/FQs*i))
     Qs.append((buf[i]-128)*np.cos(np.pi*2.0/FQs*i))

     if (i>wind):
          mk = np.sqrt(sum(Im[i-wind:i])**2 + sum(Qm[i-wind:i])**2)
          sp = np.sqrt(sum(Is[i-wind:i])**2 + sum(Qs[i-wind:i])**2)
          print (mk,end=",");print (sp)

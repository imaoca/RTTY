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

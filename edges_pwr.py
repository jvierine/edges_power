import numpy as n
import matplotlib.pyplot as plt


a=n.genfromtxt("water_229.txt")

P=10.0**(a[:,5:6558]/10.0)
P2=n.copy(P)

fvec=n.linspace(40,80,num=P.shape[1])
tvec=n.arange(P.shape[0])

plt.pcolormesh(tvec,fvec,n.transpose(P),cmap="jet",vmin=2300,vmax=4500)
plt.colorbar()
plt.show()

fwin=n.repeat(1/10,10)
FW=n.fft.fft(fwin)
for fi in range(P.shape[1]):
    P2[:,fi]=P[:,fi]-n.median(P[:,fi])

plt.pcolormesh(tvec,fvec,n.transpose(P2),cmap="jet")
plt.colorbar()
plt.show()





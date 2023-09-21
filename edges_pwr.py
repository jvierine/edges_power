import numpy as n
import matplotlib.pyplot as plt
import stuffr

t0=stuffr.date2unix(2022,1,1,0,0,0)

f=open("water_229.txt","r")
dts=[]
for l in f.readlines():
    s=l.split(" ")
    ds=s[0].split(":")
    #print(s[0])
    #    print(ds[1])
    secs=float(ds[2])*60*60 + float(ds[3])*60 + float(ds[4])
    dts.append(stuffr.unix2date(t0+float(ds[1])*24*3600.0 + secs))

    print(stuffr.unix2datestr(t0+float(ds[1])*24*3600.0 + secs))

a=n.genfromtxt("water_229.txt")

P=10.0**(a[:,5:6558]/10.0)
P2=n.copy(P)

fvec=n.linspace(40,80,num=P.shape[1])
tvec=n.arange(P.shape[0])

fig,axs=plt.subplots(2,1,layout="constrained")
p=axs[0].pcolormesh(dts,fvec,n.transpose(P),cmap="jet",vmin=2300,vmax=4500)
axs[0].set_xlabel("Time (UT)")
axs[0].set_ylabel("Frequency (MHz)")
cb=fig.colorbar(p,ax=axs[0])
cb.set_label("Noise temperature (K)")
#plt.colorbar()
#plt.show()

fwin=n.repeat(1/10,10)
FW=n.fft.fft(fwin)
for fi in range(P.shape[1]):
    mp=n.median(P[:,fi])
    P2[:,fi]=(P[:,fi])/mp

p=axs[1].pcolormesh(dts,fvec,n.transpose(P2),cmap="jet")
cb=fig.colorbar(p,ax=axs[1])
cb.set_label("$T_1(f,t)$")
axs[1].set_xlabel("Time (UT)")
axs[1].set_ylabel("Frequency (MHz)")
plt.savefig("edges_devon.png",dpi=400)
#.colorbar()
plt.show()





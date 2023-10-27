
from numpy import sum,random
import pandas as pd
import numpy as np
import math 
import seaborn as sns
import matplotlib.pyplot as plt

#ucitava sve podatke iz fajla
podaci=pd.read_csv("test.csv" )

#na prazna mjesta u koloni absences postavlja nule
podaci['absences'][podaci['absences'].eq(' ')]='0'
podaci['absences']= pd.to_numeric(podaci['absences'])

#srednja vrijednost za broj izostanaka studenata
E = sum(podaci['absences'])/len(podaci)
print(E)
var= sum((podaci['absences']-E)**2)/(len(podaci)-1)
print(var)

#standardna devijacija 
sd=math.sqrt(var)
print(sd)

#izbacuje iz analize podatke koji se nalaze izvan intervala sd
podaci1=podaci.drop(podaci[podaci.absences>(E+sd)].index)

#srednja vrijednost za broj izostanaka studenata koji su slusali predmet
E1= sum(podaci1['absences'])/len(podaci)
var1= sum((podaci1['absences']-E1)**2)/(len(podaci)-1)
sd1=math.sqrt(var1)
podaci2=pd.read_csv("test.csv")

#na prazna mjesta ubacuje vrijednost koja se najcesce ponavlja
podaci2['absences'][podaci2['absences'].eq(' ')]=int(E1)
podaci2['absences']= pd.to_numeric(podaci2['absences'])
podaci3=podaci2.drop(podaci2[podaci2.absences>(E+sd)].index)
n=len(podaci3)

#pravljenje novih kolona kako bi izracunali vjerovatnocu da student
#dobije deset ako je izostao sa 10 ili vise sati predavanja
podaci3["Ocjena_10"]= np.where(podaci3['G3']>=16,1,0)
podaci3["Puno_izostanaka"]= np.where(podaci3['absences']>=10,1,0)
podaci3["Brojac"]=1
podaci4=podaci3[["Ocjena_10", "Puno_izostanaka", "Brojac"]]
tabela=pd.pivot_table(
    podaci4,
    index=["Ocjena_10"],
    columns=["Puno_izostanaka"],
    values="Brojac",
    aggfunc=np.size    
    )
P_A=(35+3)/(276+35+32+3)
print(P_A)
P_B=(32+3)/(276+35+32+3)
print(P_B)
P_AB=3/(276+35+32+3)
print(P_AB)
P_A_B=P_AB/P_B
print(P_A_B)
E2= sum(podaci3['absences'])/n
var2= sum((podaci3['absences']-E2)**2)/(n-1)
sd2=math.sqrt(var2)


#histogram
n1=100000
X=random.normal(E2,var2, size=n1)
sns.distplot(X, hist=True, kde=False)
plt.grid()
plt.title(" Normalna raspodjela")
plt.xlabel("x")
plt.ylabel("fx(x)")
plt.show()
k=podaci3["Ocjena_10"]
plt.hist(k)
plt.xlabel("1 - studenti koji su dobili ocjenu 10")
plt.ylabel("Broj studenata")
plt.grid()

plt.figure(2)
k1=P_A_B
plt.hist(k1)
plt.title("Vjerovatnoća da je student dobio ocjenu 10 na predmetu ako je izostao sa 10 ili više sati predavanja")
plt.grid()


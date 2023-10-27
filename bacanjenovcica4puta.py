
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
#rand

def BacanjeNovcica4puta (br):
  i=0;
  ishod=np.zeros(br, dtype=int)
  while i<br:
     j=0
     pom=0
     while j<4:
         novcic=np.ceil(2*random.rand(1))
         if novcic==1:
             pom=pom+1
         j=j+1
     ishod[i]=pom
     i=i+1;
  return ishod;

N=1000
rezultat = BacanjeNovcica4puta (1000)
n2=np.count_nonzero(rezultat==2)
p2=n2/N
plt.subplot (2,1,1)
plt.stem(np.arange(1000),rezultat )
plt.title ("Simulacija eksperimenta bacanja novcica")
plt.xlabel ("N- broj bacanja ")
plt.ylabel ("Ishod simulacije")
plt.grid ()
plt.tight_layout()


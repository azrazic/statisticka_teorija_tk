import numpy as np
from numpy import random
import matplotlib.pyplot as plt
#rand

def BacanjeNovcica (br):
  i=0;
  ishod=np.zeros(br, dtype=int)
  while i<br:
     ishod[i]=random.rand(1)<0.5
     if ishod[i]==True:
         ishod[i]=0;
     else:
         ishod[i]=1
     i=i+1;
  return ishod;

A= BacanjeNovcica(1000)
n1=np.count_nonzero(A==1)
print(n1)
p1=n1/1000;
print(p1)
print(A)
plt.stem(A, use_line_collection=True)   
plt.xlabel("Broj bacanja")
plt.ylabel("Ishod eksperimenta")
plt.grid()
plt.tight_layout()
     

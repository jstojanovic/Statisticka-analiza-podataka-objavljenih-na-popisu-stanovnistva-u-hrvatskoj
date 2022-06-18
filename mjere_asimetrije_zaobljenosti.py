import statistics
from scipy import *
import scipy.stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

zad2=pd.read_excel('brojPopisanihOsoba2021PozeskoSlavoskaZupanija.xls', sheet_name='Sheet1')
podaci2=zad2['broj_popisanih'].tolist()

#osnovne znacajke:
print('Duljina uzorka: ', len(podaci2))
aritm_sredina=statistics.mean(podaci2)
print('Aritmetička sredina: ', aritm_sredina)
from statistics import mode
mod=statistics.mode(podaci2)
print('Mod: ', mod)
from statistics import median
medijan=statistics.median(podaci2)
print('Medijan: ', medijan)
kvartil1=np.percentile(podaci2,25)
kvartil3=np.percentile(podaci2,75)
print('1. kvartil: ', kvartil1)
print('3. kvartil: ', kvartil3)
st_dev=statistics.pstdev(podaci2)
print('Standardna devijacija: ', st_dev)

#mjere asimetrije:
print('Koeficijent asimetrije: ', scipy.stats.skew(podaci2,axis=0,bias=True))
print('Pearsonova mjera asimetrije S_k1: ', (aritm_sredina-mod)/st_dev)
print('Pearsonova mjera asimetrije S_k2: ', 3*(aritm_sredina-medijan)/st_dev)
print('Bowleyeva mjera asimetrije: ', (kvartil1+kvartil3-2*medijan)/(kvartil3-kvartil1))

#mjera zaobljenosti:
cetvrti_moment=0
for i in range(0,len(podaci2)):
	cetvrti_moment=cetvrti_moment+(podaci2[i]-aritm_sredina)**4
cetvrti_moment=cetvrti_moment/len(podaci2)
alpha=cetvrti_moment/st_dev**4
print('Koeficijent zaobljenosti: ', alpha)

#procjena očekivanja populacije:
mu=aritm_sredina
print('Očekivanje populacije: ', mu)
#procjena standardne devijacije populacije:
n=len(podaci2)
s=statistics.stdev(podaci2)
import math
print('Standardna devijacija populacije:', s*math.sqrt(n/(n-1)))

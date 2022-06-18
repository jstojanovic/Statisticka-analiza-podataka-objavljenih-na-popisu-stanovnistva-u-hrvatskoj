import statistics
import scipy as sp
import scipy.stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#pozivamo podatke iz Excel dokumenta
zad1=pd.read_excel('brojPopisanihOsoba2021PozeskoSlavoskaZupanija.xls', sheet_name='Sheet1')
podaci1=zad1['broj_popisanih'].tolist()

#osnovni podaci:
print('Duljina uzorka: ', len(podaci1), '\n')
print('Najmanji podatak: ', min(podaci1))
print('Najveći podatak: ', max(podaci1))
print('Rang: ', max(podaci1)-min(podaci1))
print('Aritmetička sredina: ', statistics.mean(podaci1))
from statistics import mode
print('Mod: ', statistics.mode(podaci1))
print('1. kvartil: ', np.percentile(podaci1,25))
print('3. kvartil: ', np.percentile(podaci1,75))
from statistics import median
print('Medijan: ', statistics.median)

#suma apsolutnih odstupanja:
suma=0
for i in range(0,len(podaci1)):
	suma=suma+abs(podaci1[i]-statistics.mean(podaci1))
print('Suma apsolutnih odstupanja:', suma)

#prosjecno apsolutno odstupanje:
print('Prosječno apsolutno odstupanje:', suma/len(podaci1))

#ostale mjere disperzije:
print('Varijanca: ', statistics.pvariance(podaci1))
print('Standardna devijacija: ', statistics.pstdev(podaci1))
print('Korigirana varijanca: ', statistics.variance(podaci1))
print('Korigirana standardna devijacija: ', statistics.stdev(podaci1))
print('9. percentil: ', np.percentile(podaci1,9))
print('40. percentil: ', np.percentile(podaci1,40))
print('75. percentil: ', np.percentile(podaci1,75))
#provjera:
zad1.describe()

#tablica razreda:
from tabulate import tabulate
sirina_razreda=(max(podaci1)-min(podaci1))/10
sirina_razreda

#tablica frekvencija:
zad1.value_counts()

#nastavljamo s tablicom razreda:
#trazimo zavrsne vrijednosti razreda:
zavrsne_vr_razreda=[]
v1=min(podaci1)+sirina_razreda
zavrsne_vr_razreda.append(v1)
for i in range(1,10):
    v=zavrsne_vr_razreda[i-1]+sirina_razreda
    zavrsne_vr_razreda.append(v)

#trazimo frekvencije podataka koji su u pojedinom razredu:
frekv=[]
#popunjavamo prvi razred:
brojac=0
for j in podaci1:
	if j<zavrsne_vr_razreda[0]:
		brojac=brojac+1
frekv.append(brojac)

#popunjavamo ostale razrede:
for i in range(1,10):
	br=0
	for j in podaci1:
		if zavrsne_vr_razreda[i-1] < j <= zavrsne_vr_razreda[i]:
			br=br+1
	frekv.append(br)


#trazimo relativne frekvencije podataka koji su u pojedinom razredu:
rel_frekv=[]
for i in frekv:
	rel_frekv.append(i/len(podaci1))


#kreiramo tablicu:
tablica={'RAZRED': list(range(1,11)), 'ZAVRŠNA VRIJEDNOST RAZREDA': zavrsne_vr_razreda, 'FREKVENCIJA': frekv, 'RELATIVNA FREKVENCIJA': rel_frekv}
print(tabulate(tablica, headers='keys'))

#histogram frekvencija:
hist=plt.hist(podaci1,bins=10)
plt.title('Histogram frekvencija')
plt.xlabel('Vrijednost')
plt.ylabel('Frekvencija')
plt.grid(axis='y',alpha=0.75)

#histogram relativnih frekvencija:
fig = plt.figure()
rel = plt.hist(podaci1, weights=np.zeros_like(podaci1) + 1. / len(podaci1))
plt.xlabel('Vrijednost')
plt.ylabel('Relativna frekvencija')
plt.title('Histogram relativnih frekvencija')
plt.show()
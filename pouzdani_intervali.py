import statistics
from scipy import *
import scipy.stats
from scipy.stats import t
from scipy.stats import chi2
from scipy.stats import f
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#intervali pouzdanosti
#Zadatak 1.
#podaci:
n=277
x=235.22743682310468
s=1090.9510720299668
#(a):
interval1=scipy.stats.t.interval(alpha=0.95, df=n-1, loc=x, scale=s) 
#Zadatak 2.
#podaci:
n=277
x=235.22743682310468
s=1090.9510720299668
#(b):
interval2=scipy.stats.t.interval(alpha=0.85, df=n-1, loc=x, scale=s) 

#testiranje hipoteza
#Zadatak 1.
#podaci:
mu=1
sigma=0.03
n=12
x=0.97
s=0.04
alpha=0.05

#test varijance:
#kriticna vrijednost:
critical_chi = chi2.ppf(1-alpha, n-1)
#vrijednost:
chi_exp=(n-1)*((s*s)/(sigma*sigma))
if chi_exp < critical_chi:
	print('Prihvaćamo hipotezu H0')
	a=1
else:
	print('Ne prihvaćamo hipotezu H0')
	a=0

#test ocekivanja:
#kriticna vrijednost:
critical_t= t.ppf(1-alpha,n-1)
#vrijednost:
t_exp=(x-mu)/(s/math.sqrt(n))
if abs(t_exp) < critical_t:
	print('Prihvaćamo hipotezu H0')
	b=1
else:
	print('Ne prihvaćamo hipotezu H0')
	b=0

#Jesu li rezultati mjerenja u skladu s deklaracijom?
if a==1 and b==1:
	print('Rezultati mjerenja su u skladu s deklaracijom!')
else:
	print('Rezultati mjerenja nisu u skladu s deklaracijom!')

#Zadatak 3. 

#podaci:
n1=8
x1=12.56
s1=1.36
n2=11
x2=13.01
s2=0.84
alpha=0.05

#test varijance:
#kriticna vrijednost:
critical_f=f.ppf(1-alpha,n1-1,n2-1)
f_exp=(s1*s1)/(s2*s2)
if f_exp < critical_f:
	print('Prihvaćamo hipotezu H0')
	a=1
else:
	print('Ne prihvaćamo hipotezu H0')
	a=0

#test ocekivanja:
#kriticna vrijednost:
critical_t=t.ppf(1-alpha,n1+n2-2)
t_exp=(x1-x2)/math.sqrt(((n1-1)*s1*s1)/(n1+n2-2))*math.sqrt((n1+n2)/(n1*n2))
if abs(t_exp) < critical_t:
	print('Prihvaćamo hipotezu H0')
	b=1
else:
	print('Ne prihvaćamo hipotezu H0')
	b=0

#Jesu li velicine slicne?
if a==1 and b==1:
	print('Veličine su slične, ne razlikuju se bitno!')
else:
	print('Veličine nisu slične; bitno se razlikuju!')

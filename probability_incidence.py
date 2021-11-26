#!/usr/bin/env python3.8
import math 

#Acro Yoga Event
#vybirame alespon jednoho nakazeneho
#7-dennni incidence
incidence_7d = 300 

#pravdepodobnost vyskytu nemoci
d = 5 #uvazujme nakazlivou osobu po nekolik dni
p = d * (incidence_7d / 7) /100000 
n = 100
k = 0

#Bernoulliho posloupnost
#P(Ak) = (n over k) * p**k * (1-p)**n-k
result = 1 - (p**k) * (1-p)**(n-k) #alespon jeden
print(result)
#vysledek: 10,8% pri incidence_7d = 200
#19,3% pri incidence_7d = 300


#Tydenni Yoga 
#vybirame alespon jednoho nakazeneho
#7-dennni incidence
incidence_7d = 300 

#pravdepodobnost vyskytu nemoci
d = 5 #uvazujme nakazlivou osobu po nekolik dni
p = d * (incidence_7d / 7) /100000 
n = 7
k = 0 

#Bernoulliho posloupnost
#P(Ak) = (n over k) * p**k * (1-p)**n-k
result = 1 - (p**k) * (1-p)**(n-k)
print(result)
#vysledek: 0,008
#uvazujeme kumulativni soucet nakazlivych osob po dobu poslednich 4 dnu: 10,21%
#vysledek 1,4%

# po dobu pul roku
result * 25
# 20 %
#37,6%
 
# Acro Yoga ve skupine 20ti osob
incidence_7d = 300 
d = 5 #uvazujme nakazlivou osobu po nekolik dni
p = d * (incidence_7d / 7) /100000 
n = 20
k = 0 
result = 1 - (p**k) * (1-p)**(n-k)
print(result)
#vysledek: 2,2 %
#vysledek: 4,2 %

#ucinnost testu



#monitory
a = math.sqrt(2560**2 + 1440**2) 

b = math.sqrt(1920**2 + 1200**2) 

c = math.sqrt(1920**2 + 1080**2) 

print("a: ", a, a/27, "b ", b, b/24.1, "c ", c, c/23.8)
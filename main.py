# Artjom Pushkar / 2506063540
from __future__ import print_function
from bdb import Breakpoint
from random import *
from ast import Break, While
import random 
import operator
import functools

print("-------------Veldu lið-------------")
print("Slembitölur #1 [1]")
print("Slembitölur #2 [2]")
print("Meðaltal [3]")
print("Hlaupaár [4]")
print("Hrópmerk [5]")
print("While spurningar [6]")
print("Hætta [999/0]")
val=input("Veldu lið = ")
""" 
Lidur 1: Slembitölur 1
 Útfærðu forrit sem skrifar 20 slembitölur á skjáinn á bilinu 1 – 10. Tölurnar eiga að koma í einni röð og 
tvípunkt á milli. Ekki á að vera tvípunktur eftir síðustu tölunni td. ( 7 : 4 : 8 : 2 : 9 : 10 : 1 : 5 : 6 : 3 ) Forritið 
spyr síðan hvort endurtaka eigi vinnsluna eða ekki. Ef því er svarað játandi er vinnslan endurtekin þar til 
að notandi svarar spurningunni neitandi.
"""

if val == "1":
    while True:
        teljari = 1
        start = 1 
        endir = 10 
        fjoldi_talna = 20
        for i in range(20):
            tala = randint(start, endir)
            print(tala, end=" : ")
        else:
            print(tala, end=" ")
        teljari = teljari + 1
        print("")
        svar = input("\n Viltu Gera aftur? [y/n]")
        if svar == 'n':
            print("")
            break
        elif svar == 'y':
            print("\n")
        else:
            print("\nVilla með inslatt")
            break


"""
# Lidur 2: Slembitölur 2
Útfærðu forrit sem vinnur með 50 slembitölur á bilinu 20 – 100. Í þessum lið á forritið að a ) reiknar 
meðaltal talnanna og skrifa á skjá með 1 aukastaf b ) finna lægstu töluna og skrifa á skjá c ) telur hversu 
oft tala tölur lægri en 60 koma upp og skrifa á skjá. Forritið spyr síðan hvort endurtaka eigi vinnsluna eða 
ekki. Ef því er svarað játandi er vinnslan endurtekin þar til að notandi svarar spurningunni neitandi.
"""

if val == "2":
    while True:
        teljari = 1
        start = 20 
        endir = 100 
        res=0.0
        num=4
        laegt = 100    
        teljari2 = 0
        for i in range(50):
            tala = randint(start, endir)
            if tala < laegt:
                laegt = tala
            if tala < 60:
                teljari2 += 1
        
        res += random.uniform(start, endir)

        ras = res / num

        print("\nMeðaltalið er = " + str(round(res,1)))
        print("Lægsta tala er = ", laegt)
        print("Tölur undir 60 komu  = ", teljari2, "sinnum")
        
        svar = input("\n Viltu Gera aftur? [y/n] = ")
        if svar == 'n':
            print("")
        elif svar == 'y':
            print("\n")
        else:
            print("\nVilla með inslatt")
            break
        print("\n")

"""
# Lidur 3: Meðaltal
 Útfærðu forrit sem biður notanda um að slá inn 5 heiltölur. Forritið reiknar svo meðaltal talnanna. 
Hér á að nota lykkju til að leysa verkefnið ekki vera með 5 input(). Svara skal með 1 aukastaf. Forritið 
spyr síðan hvort endurtaka eigi vinnsluna eða ekki. Ef því er svarað játandi er vinnslan endurtekin þar til 
að notandi svarar spurningunni neitandi.
"""

if val == "3":
    on = True
    while on:
        tel = 0
        summa = 0 
        while tel < 5:
            tala = int(input("Gefðu tölu: "))
            summa = summa + tala
            tel = tel + 1
        medalt = summa / tel
        print("Meðaltal = ", medalt)
        svar = input("\n Viltu Gera aftur? [y/n] = ")
        if svar == 'n':
            on = False
        elif svar == 'y':
            print("\n")
        else:
            print("\n Villa með inslatt")
        break
print("\n")

"""
# Lidur 4: Hlaupaár
 Útfærðu forrit sem biður notanda um að slá inn ártal. Forritið athugar síðan hvort viðkomandi ártal er 
hlaupaár eða ekki og skrifar á skjáinn viðeigandi skilaboð. Hér eru reglur um hlaupaár (hlaupaár er fjórða 
hvert ár nema um aldamót sé að ræða. Fjórðu hver aldamót eru svo aftur hlaupaár). Forritið spyr síðan 
hvort endurtaka eigi vinnsluna eða ekki. Ef því er svarað játandi er vinnslan endurtekin þar til að notandi 
svarar spurningunni neitandi.
"""
if val == "4":
    year = int(input("Skrifaðu ár: "))
    if year % 4 == 0:
        if year % 4 == 0 or year % 100 == 0 and year % 400:
            print("Þetta er hlaupaár!")
    else:
        print("Þetta var ekki hlaupaár")
        svar = input("\n Viltu Gera aftur? [y/n] = ")
    if svar == 'n':
        on = False
    elif svar == 'y':
        print("")
    else:
        print("\n Villa með inslatt")


"""
# Lidur 5: Hrópmerk ( factorial )
 Útfærðu forrit sem biður notandann um að slá inn heiltölu. Virkni forrits er síðan þannig að forritið tekur 
töluna sem slegin er inn segjum t.d. ef talan 4 er slegin inn og margfaldar saman rununa 4 * 3 * 2 * 1. 
Svarið ætti því að vera 24 þar sem 4 * 3 * 2 * 1 = 24. Forritið margfaldar sem sagt saman talnarununa frá 
tölunni sem slegin er inn alveg niður í 1. Annað dæmi, ef talan 6 er slegin inn reiknar forritið 6 * 5 * 4 * 3 
* 2 * 1 og forrit ætti að svara 720. Forritið spyr síðan hvort endurtaka eigi vinnsluna eða ekki. Ef því er 
svarað játandi er vinnslan endurtekin þar til að notandi svarar spurningunni neitandi
"""

if val == "5":
    on = True
    while on:
        numb = int(input("Skrifaðu tölu: "))
        numb2 = numb + 1
        margfal = list()
        for i in range (numb, 0, -1):
            margfal.append(i)
            print(i)
        nidurst = functools.reduce(operator.mul, margfal, 1)
        print(nidurst)
        svar = input("\n Viltu Gera aftur? [y/n] = ")
        if svar == 'n':
            on = False
        elif svar == 'y':
            print("")
        else:
            print("\n Villa með inslatt")
        break
       
print("\n")

"""
# Lidur 6: Spurningar um while
 Hér fyrir neðan sérðu tvær while lykkjur. Þú átt að útskýra í stuttu og hnitmiðuðu máli hvað hvor lykkjan 
fyrir sig keyrir á skjáinn. Settu svarið í print skipun þannig að svarið komið á skjáinn þegar liður 6 er valin 
í valmynd.
"""
if val == "6":
    #i=0
#while i != 10:
#    i = i + 1
#    print(i)

    print("Í fyrsta kóðanum gerist eftirfarandi: í fyrstu línunum er stafnum (i) gefið gildið 0, eftir það í gegnum strenginn (While) er það gert að skilja að þar til númerið okkar verður 10 mun það stöðva vinnu sína (i = i + 1) í þessari línu 1 er bætt við til að fá lokatöluna (print(i, end=" ")) í þessu linu muna birtast tölur 1-10,  og línur 2-4 munu endurtaka verk sín þar til þau eru orðin 10")
    print("\n")

#i=0
#while i != 10:
#    i = i + 2
#    print(i)

    print("Í þessum kóða (nr2) gerist eiginlega það sama, nema það bætist 2 i stað fyrir 1")



if val == "999" or "0":
    print("Takk fyrir notkun forritans")
Breakpoint

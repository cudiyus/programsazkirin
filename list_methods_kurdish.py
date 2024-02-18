# -*- coding: utf-8 -*-
"""----------------------------------------- lîst çi ye ?----------------------------------------------------------"""

peyv = ["argeş","bagok","cudî","dewran"]
hejmar = [23, 27, 29, 31]

# 1- >< insert() >< hûn bixwazin navekî têxin serê lîsteyê ev metod tê bikaranîn.
peyv.insert(0,'mem')    #berî bêhnokê hûn kîjan îndexê binusin wê ew peyv têkevê pêşya wê
print(peyv)

# 2- >< append() >< hûn bixwazin navekî têxin dawîyê ev metod tê bikaranîn.
peyv.append("dawî")
print(peyv)

# 3- >< remove() >< ji bo jêbirinê tê bikaranîn.
peyv.remove("bagok")
print(peyv)

# 4- >< sort() >< lîsteya te li gorî alfabeyê tê rêzkirin
peyv.sort()
print(peyv)
hejmar.sort()   #ji bo jimara jî tê bikaranîn 
print(hejmar)

# 5- >< split() >< em bixwazin strîngekê bikin lîste .
string = "mêrdîn,batman,riha"
nu = string.split(",") # dinava neynuka de tu çi binusê wê lîste ji wê de bê qutkirin.
print(nu)

# 6- >< min û max >< li ser navê xwe ye jimara biçûk û a mezin.
biçuk = min(hejmar)
mezin = max(hejmar)
print(biçuk, mezin)

# 7- >< count() >< di lîsteyê de çi heye mînak di lîsteya hejmar de gelo 31 heye ka mêze kin
hejmar = hejmar.count(31) #yek tenê heye 
print(hejmar)

# 8- >< clear >< ew jî hemû tiştî pak dike
peyv.clear()
print(peyv)

# 9- lîstekê nû bîxwaz û wa têx lîstekê nû
yek = []
du = input("yek: ")
yek.append(du)
print(du)

"""----------------------------------------îro jî bes e :]-----------------------------------------------"""
# ++++++++++++++++++++++++++++++++++++ bimînin dixweşîyê +++++++++++++++++++++++++++++++++++++++++++++++++++
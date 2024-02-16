             # array çi ye
"""wexta ku em bixwaz in ka dinava vê strîngê de çend karaket hene anjî karaktera fîlan jimar çi ye."""
         #karakter ji sifirê dest pê dike

#---------------------------------------------------------------------------------------------------------------------------

website ="https://www.şaredariyamerdin.com"
nasin = "merdin paytexta kurda ye. cihe şer u merda ye :)"


# 1- di nava 'nasin' de çend  karakter he ne?
hesab = len(nasin)
print(hesab) #ji mere dibêje 48 karakter hene

# 2-di nava "websîte" de karakterên www di termîlê de nîşan bike
hesab2 = website[8:11] #ji bo îndeksê ku tu bîxwazê paranteza bi goşe binuse.
print(hesab2)

# 3-di nava websîte de "com" di termînalê de nîşan bide
hesab2 = website[-3:] #yan jî [29:31]
print(hesab2)

# 4- di nava nasîn ê de peyva Kurd di termînalê de nîşan bide.
hesab = nasin[16:20] # tenê wê KURD bê nîşankirin :) an jî [16:-28] jî çêdibe
print(hesab)

# 5- nasîn ê strînga zo binuse
hesab = nasin[::2] #tîpekê dinuse yekê nanivîsê heta dawî diçe
print(hesab)

# 6-strîngê ters nîşan bike
hesab = nasin[::-1]
print(hesab)

# 7-strînga "slav dinya" de tîpa d'yê girs bike(D)
peyv = "slav dinya"
peyv = peyv[0:5] + "D" + peyv[-4:] 
print(peyv)

# 8- navê "cudîyus" 3 derba di termînalê de nîşan bike
nav ="cudiyus " * 3
print(nav)

#belê îro hevqas bes :)
#                                   em ê îro ji were behsa metodên strînga bikin
"""----------------------------------------------------------------------------------------------------------------------"""
# -*- coding: utf-8 -*-  
"""  >>>>  heger hûn rêza 3. di koda xwe de binusin wê demê hûn karin kodê xwe bi kurdî binivîsin :)   <<<<  """


peyam = "slav navê min mem. ez niha li Amedê me. "
print(peyam)

# 1- teknîka >< upper() ><  upper di nava strînga we de hemû karakteran dike tîpên girs.
peyam = peyam.upper()
print(peyam)

# 2- teknîka >< lower() >< lower di nava strînga we de peyva tev hûr dike.
peyam = peyam.lower()
print(peyam)

# 3- teknîka >< title() >< title di nava strînga we da her tîpên serê peyvê girs dike û peyvê dî tev hûr in. 
peyam = peyam.title()
print(peyam)

# 4- teknîka >< capitalize() >< capitalize di nava strîngê de tenê peyva pêşî girs nîşan dide êdî tev hûr in.
peyam = peyam.capitalize()
print(peyam)

# 5- teknîka >< strip() >< heger di strîngê de pêşîya wê valahî hebê strip wê valahîyê di termînalê de jê dibe. ji boş şîfreya tê bikaranîn.
peyam2 = "  avanî."
peyam2 = peyam2.strip()
print(peyam2)

# 6- teknîka >< split() >< di strîngê de ji cîhê valahîya di termînalê de apostrof tê nîşankirin(peyama perço perço dike.)
peyam = peyam.split()
print(peyam)  #bi şiklekî dî je ew dibin array û tu karê va array'a di termînalê de nîşan bike mînak rêza 34.
print(peyam[3]) #peyva 2. şanî te dide mem nîşan dide

# 7- teknîka >< join() >< splît dîsa dibê wek berê.
peyam = ' '.join(peyam) 
#apostrof tev pak dibin ji ber wilo min di nava apostrofê valahîyek çêkir wateya wê dibê apostrofa rak valahîyê deyn wir.
print(peyam)

# 8- teknîka >< find() ><
"""mînak ez dixwazim bê di strînga me da peyva Amed heye an na. wê demê em teknîka find bi kar tînin
lê teknîka find li ser îndexa li wê peyvê digere heger ew peyv hebe bi jimareke pozîtîf dibe ew îndexa 30.'e lê heger ew peyv di strîngêda
nebe ji tere jimareke negatîf nîşan dide. ka em binusin."""
index = peyam.find('amed')
print(index)

# 9- teknîka >< startswitch() >< heger tu bixwaze strînga te bi çi tîpê destpê dike ev teknîk tê bikaranîn true an false nîşan dide.
  #endswitch jî dibêje ev strîng bi kîjan tîpê xilas bû ye.
destpek = peyam.startswith('S')  #girs an jî hûr bê jî ferq dike heger min tîpa s hûr binusa wê demê wê false bigota.
print(destpek) 

# 10- teknîka >< replace() >< peyva diguherêne mînak ez ê Amed jê derxim û Merdîn binivîsim.
peyam = peyam.replace('amedê','Mêrdînê')
print(peyam)

"""--------------------------HEVALNO TEKNÎKÊN STRÎNGA GELEK IN MIN JI WERE 10 METHOD NIVÎSAN Ê DÎN JÎ HÛN BIBÎNÎN-------------------"""
#-------------------------------------------------- Bimînîn di xweşîyê de ---------------------------------------------------
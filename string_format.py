"""di strînga de format çawa tê bikar anîn"""

nav = "mem"
pasnav = "akar"
print("nave min {} {}".format(nav, pasnav))
"""di nava îndeksade hûn dikarin refê stringa binusin. mînak rêza 8. ez şanî we bidim. """
print("nave min {0} {1}".format(nav,pasnav))
"""heger hûn cîhê 0 û 1'ê biguherin wê demê wê cîhê nav û paşnavê we biguherê. mînak rêza 9. ez şanî we bidim. """
print("nave min {1} {0}".format(nav,pasnav))
"""hûn dikarin ji cîhê hejmara lî cema strînga we bi tîpa jî nîşan bikin. mînak rêza 11. ez şanî we bidim. """
print("nave min {n} {p}".format(n=nav,p=pasnav))
"""ka em ji were hejmareke float jî têxin nava formatê """
hejmar = 200 / 700
print("jimara te: {:1.4}".format(hejmar))
"""ev hejmara me jimareyek float e. heger em di nava paranteza xemilandî de{}  tiştekî nenivîsin wê ev hejmar 0.2857.... û wisa dîçê 
lê belê heger tu dî nava paranteza xemilandî de {:1.4} binusê wateya wê ez bêjim.
duxaltok : >> tu ji kompîtirê re dibeje ez vê dixwazim
wateya hejmara :1 yanî valahîyekê berî vê hejmarê çêke,heger tu ji cîhê 1 ê 10 binusê wê demê wê 10 kêm hejmara wê valahîyê bihêle.
ew xaltok dibêje ku pîştre vîrgulê hevqas jimara şanî min bide[0,2857] """
#format bi şiklekî dî jî çêdibe.mînak rêza 21.
print(f"nave min {nav} {pasnav}") 
#heger hûn berî xalecota f binivîsîn hûn dikarin dinava paranteza xemilandî de strîngê xwe binivîsin.

#bimînin dixweşîyê de :)
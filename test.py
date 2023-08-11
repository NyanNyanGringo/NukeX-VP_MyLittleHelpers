s = """
december,NORMAL,1270,482,
SyeRaa,NORMAL,260,27,
cosmoball,NORMAL,214,111,
dva_holma,NORMAL,170,45,
otriv,NORMAL,83,13,
humorist,NORMAL,74,12,
ATTR2,NORMAL,65,47,
CHERNOVIK,NORMAL,55,10,
GK,NORMAL,45,36,
nika,NORMAL,39,19,
Podelki,NORMAL,38,22,
pereval_dtlv,NORMAL,32,8,
demo-vfx,NORMAL,31,16,
SELFIE,NORMAL,31,7,
Diversant,NORMAL,27,13,
KAMAZ,NORMAL,25,25,
ice2,NORMAL,18,22,
russian_south_series,NORMAL,15,2,
Ostin,NORMAL,13,13,
parma,NORMAL,8,8,
cheburashka,NORMAL,7,2,
ninth,NORMAL,7,2,
Diversant_trailer,NORMAL,4,1,
cheburashka_old,NORMAL,4,7,
SMALL_PEOPLE,NORMAL,3,7,
psih,NORMAL,3,2,
wof,NORMAL,2,8,
white_show,NORMAL,1,6,
Pvl,NORMAL,0,1,
Bogatyr,NORMAL,0,2,
Russian_South,NORMAL,0,4,
TN,NORMAL,0,1

"""
# 0, 4, 8, 12
names = []
types = []
sizes = []
components = []

ss = s.split(",")
for i in range(0, len(ss), 4):
    names.append(ss[i])
    types.append(ss[i + 1])
    sizes.append(ss[i + 2])
    components.append(ss[i + 3])

[print(x.replace("\n", "")) for x in names]
print()
[print(x) for x in types]
print()
[print(x) for x in sizes]
print()
[print(x) for x in components]

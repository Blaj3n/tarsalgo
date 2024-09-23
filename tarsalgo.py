# print("1. feladat")

ajto = []

with open("ajto.txt", "r", encoding="utf-8") as file:
    for egysor in file:
        egysor = egysor.strip().split()
        ajto.append([int(egysor[0]), int(egysor[1]), int(egysor[2]), str(egysor[3])])
print(ajto)

print("2. feladat")

for szemely in ajto:
    if szemely[3] == "be":
        print(f"Az első belépő: {szemely[2]}")
        break

for i in range(len(ajto) - 1, -1, -1):  # len(ajtó) - 1, tehát esetünkben 515-től megyünk -1 + 1- ig, tehát 0-ig
    # [[, -1-esével megyünk, tehát visszafele.
    if ajto[i][3] == "ki":
        print(f"Az utolsó kilépő: {ajto[i][2]}")
        break

# print(len(ajto))
# print(ajto[515])


# 9 5 9 ki

# print("3. feladat")

szemelyek = []
for szemely in ajto:
    if szemely[2] not in szemelyek:
        szemelyek.append(szemely[2])
# print(sorted(szemelyek))    # azonosítók lista rendezés növekvő sorrendbe (asc)

with open("athaladas.txt", "w", encoding="utf-8") as fajl:
    for egyelem in sorted(szemelyek):
        szamlalo = 0
        for be_ki in ajto:
            if be_ki[2] == egyelem:
                szamlalo += 1
        fajl.write(f"{egyelem} {szamlalo}\n")

szemelyek_novekvo = sorted(szemelyek)

# for valtozo in range(5): # [1, 5[ # range(kezdő, meddig menjen -1, hányasával),
# range(meddig menjen 0-tól - 1) range(5) = [0, 1, 2, 3, 4], range(2, 7) = [2, 3, 4, 5, 6], range(1, 5, 2) = [1, 3]

# HF: 4. feladat lista *
print("")
print("4. feladat")

# bent_kint = [[1, be, ki, be, ki, be], [2, be, ki, be, ki], ..., [41, be, ki, be]]
# Azt kell tudni, hogy minden egyes belépéshez tartoznia kell egy kilépésnek. De mi pont nem ezt keressük, hanem ha több belépés van (biztos 1-gyel), akkor írjuk ki az bent_kint[i] az egyelem[0].

bent_kint = []
for szemely in szemelyek_novekvo:   # szemely = 1
    szemelyek = [szemely]   # szemelyek = [szemely] --> szemelyek.append(szemely)
    for egyelem in ajto:
        if egyelem[2] == szemely:       #   HA azonosító = 1
            szemelyek.append(egyelem[3])    # szemelyek = [be, ki, be, ki, be]
    bent_kint.append(szemelyek)             # bent_kint = [[1, be, ki, be, ki, be]]
# print(bent_kint)    # [[szemely_azonosito, belépett, kilépett, belépett, kilépett, belépett]]

print(f"A végén a társalgóban voltak:", end=" ")
for szemely in bent_kint:
    if szemely.count("be") != szemely.count("ki"):
        print(szemely[0], end=" ")

print("\n")

print("5. feladat ")

jelenleg = []
mennyiseg = 0
for szemely in ajto:
    if szemely[3] == "be":
        mennyiseg += 1
        jelenleg.append(mennyiseg)
    elif szemely[3] == "ki":
        mennyiseg -= 1
        jelenleg.append(mennyiseg)
# print(jelenleg)     # az adott időben hányan tartózkodnak a helyiségben

legnagyobb_letszam = max(jelenleg)  # 12
legnagyobb_indexe = jelenleg.index(legnagyobb_letszam)  # a legnagyobb_letszam indexét keressük a jelenleg nevű listában
# print(legnagyobb_indexe)    # 143

print(f"Például {ajto[legnagyobb_indexe][0]}:{ajto[legnagyobb_indexe][1]}-kor voltak a legtöbben a társalgóban.")

print("\n")

print("6. feladat")

szemely_azonosito = input("Adja meg a személy azonosítóját! ")

print("\n")

# A feladat alapjáraton készen van, csak a végén amikor csak belépés van kilépés nincs azt az 1 időpontot nem tudom kiiratni
print("7. feladat")

for szemely in ajto:
    if str(szemely_azonosito) == str(szemely[2]) and szemely[3] == "be":
        szemely_be = f"{szemely[0]}:{szemely[1]}"
        # print(szemely_be)
    elif str(szemely_azonosito) == str(szemely[2]) and szemely[3] == "ki":
        szemely_ki = f"{szemely[0]}:{szemely[1]}"
        print(f"{szemely_be}-{szemely_ki}")
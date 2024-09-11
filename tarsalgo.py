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
print(sorted(szemelyek))    # lista rendezés növekvő sorrendbe (asc)

with open("athaladas.txt", "w", encoding="utf-8") as fajl:
    for egyelem in sorted(szemelyek):
        szamlalo = 0
        for be_ki in ajto:
            if be_ki[2] == egyelem:
                szamlalo += 1
        fajl.write(f"{egyelem} {szamlalo}\n")

# for valtozo in range(5): # [1, 5[ # range(kezdő, meddig menjen -1, hányasával), range(meddig menjen 0-tól - 1) range(5) = [0, 1, 2, 3, 4], range(2, 7) = [2, 3, 4, 5, 6], range(1, 5, 2) = [1, 3]

# HF: 4. feladat lista *

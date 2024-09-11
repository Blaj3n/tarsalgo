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
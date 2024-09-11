# print("1. feladat")

ajto = []

with open("ajto.txt", "r", encoding="utf-8") as file:
    for egysor in file:
        egysor = egysor.strip().split()
        ajto.append([int(egysor[0]), int(egysor[1]), int(egysor[2]), str(egysor[3])])
print(ajto)
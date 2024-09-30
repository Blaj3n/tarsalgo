"""
1. for i in range(y) -> x: 0-től indulunk, és y megyünk y-1-ig megyünk.
2. for i in range(x, y) -> x: kiinduló érték, y: végcél + 1 -> x-től megyünk y - 1, ebben az esetben a z == 1
3. for i in range(x, y, z) -> x: kiinduló érték, y: végcél + 1 -> x-től megyünk y - 1, z: léptető, hányasával lépjünk?
"""
print("1: 0-től 9-ig (10-1-ig) megyünk: ")
for i in range(10):
    print(i, end=" ")

print("\n")

print("2: 2-től 10-ig megyünk: ")
for i in range(2, 11):
    print(i, end=" ")

print("\n")

print("3: 4-től 20-ig megyünk 4-esével: ")
for egyelem in range(4, 21, 4):
    print(egyelem, end=" ")

print("\n")

# Az összevegyítésnél használjunk a range() függvény:
am = ["a", "m"]
la = ["l", "a"]
# len(la) == 2

# for i in range(len(la)): ==> i_1 = 0, i_2 = 1
for i in range(len(la)):
    print(f"{am[i]}{la[i]}", end="")
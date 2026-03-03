
mevalar = []
print(mevalar)


mevalar.extend(["Olma", "Banan", "Gilos"])
print(mevalar)


print(mevalar[0])


mevalar.append("Anor")
print(mevalar)


sonlar = []
for i in range(5):
    son = int(input("son kiriting"))
    sonlar.append(son)
print(sonlar)


print(mevalar[-1])


mevalar[1] = "Kivi"
print(mevalar)


mevalar.sort()
print(mevalar)


ismlar = []
for i in range(3):
    ism = input("ism kiriting")
    ismlar.append(ism)
print(ismlar)


for m in mevalar:
    print(m)
print(f"listda{len(mevalar)}ta element bor")


if "Olma" in mevalar:
    mevalar.remove("Olma")
print(mevalar)


mevalar.reverse()
print(mevalar)


mevalar.clear()
print(mevalar)



r1 = [1, 2, 3]
r2 = [4, 5, 6]
r3 = r1 + r2
print(r3)

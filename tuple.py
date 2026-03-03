bush = ()
print(bush)


k2 = ("Python", "Java", "C++")
print(k2)


print(k2[0])


list1 = []
for i in range(4):
    son = int(input("son kiriting"))
    list1.append(son)
k3 = tuple(list1)
print(k3)


for element in k2:
    print(element)


print(len(k2))


print(k2[-1])


k4 = k2 + k3
print(k4)


sonlar1 = (15, 40, 5, 60)
print(f"Eng kattasi: {max(sonlar1)}, Eng kichkinasi: {min(sonlar1)}")


print("Java" in k2)


print(k2[0:2])


print(sum(sonlar1))


print(sorted(sonlar1))


k5 = ("olma", "behi", "olma, gilos")
print(f"behi {k5.count('behi')} marta")


print(sonlar1[::-1])

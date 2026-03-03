d = {}
print(d)


d["ism"] = "Shoh"
d["yosh"] = 20
print(d)


user = {}
user["ism"] = input("Ism kiriting: ")
user["familiya"] = input("Familiya kiriting: ")
print(user)


print(d.keys())


d["shahar"] = "Jizzax"
print(d)


d["yosh"] = 21
print(d)


print(d.values())


print("ism" in d)


print(d.items())


del d["shahar"]
print(d)
 

new_d = {}
for i in range(3):
    k = input("Kalit: ")
    v = input("Qiymat: ")
    new_d[k] = v
print(new_d)


for v in d.values():
    print(v)


narx = {"olma": 5000, "anor": 8000}
print(sum(narx.values()))


d.clear()
print(d)

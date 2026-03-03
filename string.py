ism = "Shohrux"
print(ism)

ism = input("Ismingizni kiriting: ")
print(ism.lower())

familya = input("Familiyangizni kiriting: ")
print(familya.upper())

print(len("Python"))

matn = "Mehanizatsiyalashtiraolmaganliklaringizdandirda"
print(matn[0])

matn = input("Matn kiriting: ")
print(matn[-1])

s = "Salom, Dunyo!"
print(s.replace("Dunyo", "Shohrux"))


a1 = input("1-satr: ")
a2 = input("2-satr: ")
print(a1 + a2)

for belgi in "Salom":
    print(belgi)

text = "Salom"
print(text[::-1])

soz = input("Yozing: ")
print(f"Uzunligi: {len(soz)}")

katta = "Hello, Python!"
print(katta.upper())

a_matn = input("Matn kiriting: ")
print(f"a harfi {a_matn.count('a')} ta")

ism1 = "Shohrux"
print(f"Birinchi harf: {ism1[0]}, Oxirgi: {ism1[-1]}")

matn1 = input("1-matn: ")
matn2 = input("2-matn: ")
if len(matn1) > len(matn2):
    print("1-matn uzunroq")
elif len(matn2) > len(matn1):
    print("2-matn uzunroq")
else:
    print("Uzunliklari teng")

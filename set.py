a = set()
print(a)


s = {"qizil", "yashil", "ko'k"}
print(s)
 
d = set()
d.add("binafsha")
print(d)


sonlar = set()
for i in range(5):
    son = int(input('son kiriting'))
    sonlar.add(son)
print(sonlar)


for x in a:
    print(x)


print(len(a))


s.discard("qizil")
print(s)


b = {10, 20}
c = a.union(b)
print(c)


set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.intersection(set2))


d.pop()
print(d)


print(sorted(a))


print(set1.difference(set2))

s.clear()
print(s)

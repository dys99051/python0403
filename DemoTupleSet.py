# DemoTupleSet.py

a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(b)
print(type(a))
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

tp = (1,2,3)
print(type(tp))
print(tp)
print(tp.count(1))

def calc(a,b):
    return a+b, a*b

result = calc(10,11)
print(result)

# 형식 변환
a = set((1,2,3))
print(a)
b = list(a)
b.append(4)
print(type(b))
print(b)

print("------dict-----")
color = {"apple":"red","banana":"yellow"}
print(color["apple"])
color["kiwi"] = "green"
del color["apple"]
print(color)



phone = {"kim":"010-111","lee":"010-123","park":"010-567"}
for item in phone.items():
    print(item)

for k,v in phone.items():
    print(k,v)

print("park" in phone)
print("moon" not in phone)

p = phone
print(p)
print(id(phone), id(p))
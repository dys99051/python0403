# function4.py

for i in lst:
    if i > 5:
        break
    print("Item:{0}".format(i))

print("------continue-------")
for i in lst:
    if i % 2 == 0:
        continue
    print("Item:{0}".format(i))

print("------수열함수------")
print( list(range(10)))
print( list(range(10,0,-1)))
print(list(range(2000,2024)))
for i in range(5):
    print(i)
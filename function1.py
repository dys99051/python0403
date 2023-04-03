# function1.py

# 함수 정의
def setValue(newValue):
    x = newValue
    print("내부: ", x)

# 함수 호출
retValue = setValue(5)
print(retValue)

def swap(x,y):
    return y,x

retValue = swap(4,5)
print(retValue)

# 디버깅을 위한 함수(교집합)
def intersect(prelist, postlist):
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

print(intersect("SPAM","HAM"))
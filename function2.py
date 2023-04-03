# function2.py

def times(a=10, b=20):
    return a*b

print(times())
print(times(5))
print(times(5,6))

def connectURI(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

print(connectURI("www.naver.com","80"))
print(connectURI(port="80", server="www.credu.com"))

# 가변인자사용
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)

    return result

print(union("HAM","SPAM"))
print(union("HAM","EGG","SPAM"))

# 람다함수
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))
print((lambda x:x*x)(3))
print(globals())
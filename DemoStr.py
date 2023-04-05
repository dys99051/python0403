# DemoStr.py

strA = "python is very powerful"
strB = "파이썬은 강력해"
print(len(strA))
print(len(strB))
print(strA.capitalize())
print(strA.count("p"))
print(strA.startswith("python"))
print(strA.endswith("ful"))
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2680".isdecimal())

print("---문자열 공백제거---")
u = " spam and ham "
result = u.strip()
print(u)
print(result)


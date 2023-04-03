# # ifelse.py
# score = int(input("점수 입력: "))

# if 90 <= score <=100:
#     grade = "A"
# elif 80 <= score:
#     grade = "B"
# elif 70 <= score:
#     grade = "C"
# else:
#     grade = "D"

# print("등급은 ", grade)

value = 5
while value > 0:
    print(value)
    value -= 1

d = {"apple":100, "orange":200, "banana":300}
for k,v in d.items():
    print(k, v)
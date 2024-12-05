import sys

input = sys.stdin.readline
print = sys.stdout.write

a = int(input().rstrip())

# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

if a >= 90 or a >= 100:
    print("A\n")
elif a >= 80 or a >= 89:
    print("B\n")
elif a >= 70 or a >= 79:
    print("C\n")
elif a >= 60 or a >= 69:
    print("D\n")
else:
    print("F\n")

# PASSED

"""
score = "F"

if a >= 60:
    score = "D"
    if a >= 70:
        score = "C"
        if a >= 80:
            score = "B"
            if a >= 90:
                score = "A"

print(f"{score}\n")
"""

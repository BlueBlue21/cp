import sys

input = sys.stdin.readline
print = sys.stdout.write

a = int(input().rstrip())
b = int(input().rstrip())

quadrant = 1

if a < 0 and b > 0:
    quadrant = 2
elif a < 0 and b < 0:
    quadrant = 3
elif a > 0 and b < 0:
    quadrant = 4

print(f"{quadrant}\n")

# PASSED

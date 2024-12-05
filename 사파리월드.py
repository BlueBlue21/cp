import sys

input = sys.stdin.readline
print = sys.stdout.write

a, b = map(int, input().rstrip().split())

print(f"{abs(a - b)}\n")

# PASSED

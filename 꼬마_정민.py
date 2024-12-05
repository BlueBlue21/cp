import sys

input = sys.stdin.readline
print = sys.stdout.write

a, b, c = map(int, input().rstrip().split())

print(f"{a + b + c}\n")

# PASSED

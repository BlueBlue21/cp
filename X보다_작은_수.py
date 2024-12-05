import sys

input = sys.stdin.readline
print = sys.stdout.write

n, x = map(int, input().rstrip().split())
a = map(int, input().rstrip().split())

result = []

for i in a:
    if x > i:
        result.append(i)

print(" ".join(map(str, result)) + "\n")

# PASSED

# https://wook-2124.tistory.com/227

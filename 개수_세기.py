import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input().rstrip())
n_map = map(int, input().rstrip().split())
v = int(input().rstrip())

count = 0

for i in n_map:
    if i == v:
        count += 1

print(f"{count}\n")

# PASSED

# n을 사용하는 방법도 있음

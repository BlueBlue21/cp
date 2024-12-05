import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input().rstrip())

result = []

for _ in range(n):
    a, b = map(int, input().rstrip().split())
    result.append(a + b)

print("\n".join(map(str, result)) + "\n")

# PASSED

"""
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    print(f"{a + b}\n")
"""

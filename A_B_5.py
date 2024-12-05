import sys

print = sys.stdout.write

for i in sys.stdin.read().splitlines():
    a, b = map(int, i.rstrip().split())

    if a > 0 or b > 0:
        print(f"{a + b}\n")

# PASSED

"""
input = sys.stdin.readline

while True:
    a, b = map(int, input().rstrip().split())

    if a == 0 and b == 0:
        break

    print(f"{a + b}\n")
"""

import sys

print = sys.stdout.write

for i in sys.stdin.read().splitlines():
    a, b = map(int, i.rstrip().split())
    print(f"{a + b}\n")

# PASSED

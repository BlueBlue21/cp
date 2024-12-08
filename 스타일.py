import sys

input = sys.stdin.readline
print = sys.stdout.write

# 1
a = int(input().rstrip())
# 2 3
b, c = map(int, input().rstrip().split())

print(f"{a} {b} {c}\n")

abc_map = []

"""
2
1
4
3
5
"""
for i in sys.stdin.read().splitlines():
    abc_map.append(int(i))

abc_map.sort()

print(f"{" ".join(map(str, abc_map))}\n")

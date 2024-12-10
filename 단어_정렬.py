input = open(0).readline
print = open(1, "w").write

a = int(input().rstrip())
b = []

for i in range(a):
    b.append(input().rstrip())

b = list(set(b))
b.sort()
b.sort(key=lambda a: len(a))

print("\n".join(map(str, b)) + "\n")

# PASSED

# note: b.sort(key=lambda a: (len(a), a))

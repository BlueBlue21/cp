input = open(0).readline
print = open(1, "w").write

a, b = map(int, input().rstrip().split())
c = []
d = []

for i in range(a):
    c.append(list(map(int, input().rstrip().split())))

for i in range(a):
    d.append(list(map(int, input().rstrip().split())))

# for i in range(a):
#     for j in range(b):
#         print(f"{c[i][j] + d[i][j]} ")

#     print("\n")

# PASSED

# e = [[c[i][j] + d[i][j] for j in range(b)] for i in range(a)]

# for i in e:
#     print(" ".join(map(str, i)) + "\n")

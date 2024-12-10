a, b, c, d, e = map(int, open(0).readline().rstrip().split())

open(1, "w").write(f"{(a**2+b**2+c**2+d**2+e**2)%10}\n")

# PASSED

# unique = list(open(0).readline().rstrip().split())

# result = 0

# for i in range(5):
#     result += int(unique[i]) ** 2

# open(1, "w").write(f"{result % 10}\n")

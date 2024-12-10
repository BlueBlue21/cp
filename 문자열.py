input = open(0).readline
print = open(1, "w").write

for i in range(int(input().rstrip())):
    a = input().rstrip()

    print(f"{a[0]}{a[len(a) - 1]}\n")

# PASSED

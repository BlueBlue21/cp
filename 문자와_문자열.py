input = open(0).readline

s = input().rstrip()
i = int(input().rstrip())

open(1, "w").write(f"{s[i - 1]}\n")

# PASSED

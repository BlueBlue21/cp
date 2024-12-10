a, b = map(int, open(0).readline().rstrip().split())

open(1, "w").write(f"{(a + b)*(a - b)}\n")

# PASSED

# note: a**2-b**2

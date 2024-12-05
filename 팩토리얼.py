import sys

input = sys.stdin.readline
print = sys.stdout.write

a = int(input().rstrip())


def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


print(f"{factorial(a)}\n")

# PASSED

"""
import math

print(f"{math.factorial(a)}\n")
"""

import sys

print = sys.stdout.write

n_list = [0] * 30

for i in map(int, sys.stdin.read().splitlines()):
    n_list[i - 1] = 1

for i in range(len(n_list)):
    if n_list[i] == 0:
        print(f"{i + 1}\n")

# 이걸 왜 난 바보같이 풀엇는가...

# PASSED

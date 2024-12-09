import sys

print = sys.stdout.write

n_list = []

for i in sys.stdin.read().splitlines():
    n_list.append(int(i))

n_list.sort()

print(f"{" ".join(map(str, n_list))}\n")

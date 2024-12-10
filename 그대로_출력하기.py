print = open(1, "w")

for i in open(0).read().splitlines():
    print.write(f"{i}\n")

# PASSED

# open(1, "w").write(open(0).read())
# note: or use while and try

input = open(0).readline
print = open(1, "w").write

score = input().rstrip()
score_dict = {
    "A+": 4.3,
    "A0": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B0": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C0": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D0": 1.0,
    "D-": 0.7,
    "F": 0.0,
}

for k, v in score_dict.items():
    if score == k:
        print(f"{v}\n")

# PASSED

# print(f"{score_dict[input().rstrip()]}\n")

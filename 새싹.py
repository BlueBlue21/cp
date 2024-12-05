import sys

print = sys.stdout.write

flower = [
    "         ,r'\"7",
    "r`-_   ,'  ,/",
    " \\. \". L_r'",
    "   `~\\/",
    "      |",
    "      |",
]

print("\n".join(map(str, flower)) + "\n")

# PASSED

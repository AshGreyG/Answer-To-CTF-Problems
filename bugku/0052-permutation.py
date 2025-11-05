import itertools

ciphertext = "lf5{ag024c483549d7fd@@1}"
offset = [1, 2, 3, 4, 5, 6]

for perm in itertools.permutations(offset) :
    s : str = ""
    for i in range(0, len(ciphertext), 6) :
        s += "".join([ciphertext[i + j - 1] for j in perm])
    if "flag{" in s :
        print(f"{s} with permutation {perm}")

# Result is flag{52048c453d794df1}@@ with permutation (2, 1, 5, 6, 4, 3)

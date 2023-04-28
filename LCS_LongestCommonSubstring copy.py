import numpy as np

string_A = "hish"
string_B = "fish"

table = np.zeros((len(string_A), len(string_B)))

for i in range(len(string_A)):
    for j in range(len(string_B)):
        if string_A[i] == string_B[j]:
            table[i][j] = table[i-1][j-1] + 1
        else:
            table[i][j] = 0

print(table)
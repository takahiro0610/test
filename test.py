A = 10
B = 5

print(A+B)

for a in range(A):
    print(a)


import pandas as pd

C = pd.DataFrame([1,2,3],["a","b","c"])
print(C)

print(C[0]["b"])
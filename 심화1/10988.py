A = input()
rev = ""
for i in A:
    rev = i + rev
if A == rev :
    print(1)
else :
    print(0)
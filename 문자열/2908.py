num = input()
num1 = num.split()[0]
num2 = num.split()[1]

rev_num1 = ''
rev_num2 = ''
for i in num1:
    rev_num1 = i + rev_num1
for i in num2:
    rev_num2 = i + rev_num2

if int(rev_num1 > rev_num2) :
    print(rev_num1)
else :
    print(rev_num2)
    
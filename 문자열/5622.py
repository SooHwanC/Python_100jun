arr1 = ['A','B','C']
arr2 = ['D','E','F']
arr3 = ['G','H','I']
arr4 = ['J','K','L']
arr5 = ['M','N','O']
arr6 = ['P','Q','R', 'S']
arr7 = ['T','U','V']
arr8 = ['W','X','Y', 'Z']

A = input()

count = 0
for i in list(A):
    if i in arr1:
        count += 3
    elif i in arr2:
        count += 4
    elif i in arr3:
        count += 5
    elif i in arr4:
        count += 6
    elif i in arr5:
        count += 7
    elif i in arr6:
        count += 8
    elif i in arr7:
        count += 9
    elif i in arr8:
        count += 10

print(count)
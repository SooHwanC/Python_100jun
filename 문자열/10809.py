A = input()
arr = [-1] * 26
for i in range(len(A)):
    index = ord(A[i]) - 97
    if arr[index] == -1:
        arr[index] = i
        
for i in range(len(arr)):
    print(arr[i], end=" ")
    
######################

# A = input()
# B = 'abcdefghijklmnopqrstuvwxyz'

# for i in B:
#     if i in A:
#         print(A.index(i), end =' ')
#     else:
#         print(-1, end=' ')

###################

# A = input()

# for i in 'abcdefghijklmnopqrstuvwxyz':
#     print(A.find(i), end=" ")
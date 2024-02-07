num = int(input())
count = num
for i in range(num) :
  A = input()
  for j in range(len(A)-1) :
    if A[j] == A[j+1] :
      continue
    elif A[j] in A[j+1:] :
      count -= 1
      break
print(count)
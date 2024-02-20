# A, B, V = map(int, input().split())

# count = 1
# while V >= 0:
#     V -= A
#     if V <= 0:
#         break
#     V += B
#     count += 1

# print(count)    


A, B, V = map(int, input().split())
count = (V - A) // (A - B)
if (V - A) % (A - B) != 0:
    count += 1
print(count + 1)
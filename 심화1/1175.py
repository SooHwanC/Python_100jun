A = input().upper()
alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alph_dict = {char: 0 for char in alph}

for i in alph:
    for j in A:
        if i == j:
            alph_dict[i] += 1
            
max_val = max(alph_dict.values())

max_keys = [key for key, value in alph_dict.items() if value == max_val]

if len(max_keys) == 1:
    print(max_keys[0])
else :
    print('?')
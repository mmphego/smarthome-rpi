L = [1,2,4,8,16,32,64]
X = 5
found = False
i = 0

while not found and i < len(L):
    if 2 **X == L[i]:
        found = True
    else:
        i +=1
if found:
    print ('at index', i)

else:
    print (X, 'not found', i)


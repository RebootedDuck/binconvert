#convert denary to bits

binaryPlaceValues = [1,2,4,8,16,32,64,128] # There's a better way to do this but I can't be bothered

denaryStr = str(input("Enter denary number: "))
denaryInt = int(denaryStr)

denaryToList = list(map(int,denaryStr))
bitsList = [0,0,0,0,0,0,0,0]

# print(denaryToList)

'''
for x in reversed(denaryToList):
    for y in reversed(binaryPlaceValues):
        if y > x:
            pass
        elif:
            
            
            
    print(x)
'''

for y in reversed(binaryPlaceValues):
    if y > denaryInt:
        pass
    else:
        print(binaryPlaceValues.index(y))
        bitsList[binaryPlaceValues.index(y)] = 1
        denaryInt = denaryInt - y

# print(bitsList)

bitsListRev = list(reversed(bitsList))

print(bitsListRev)

# TODO: Auto-scale bitsList size, error handling, from binary to denary, handle negative numbers, use bitLists properly, auto calculate
#       binary place values, not have awful strings

def findLargestPowerOfTwo(inputInt: int):
    power = int(2)
    while power < inputInt:
       power = power * 2 
    
    return power

def findNeededBitsToStoreInt(inputInt: int):
    quantity = int(1)
    power = int(2)
    
    while power <= inputInt:
        power = power * 2
        quantity = quantity + 1
        
    return quantity

def returnListOfPowersOf2(inputInt: int):
    powers = [1,2]
    power = int(1)
    
    while power < inputInt:
        power = power * 2
        if not power in powers:
            powers.append(power)
            
    return powers
    
    
def convertIntToBits(inputInt: int):
    binaryPlaceValues = returnListOfPowersOf2(inputInt)
    bitsList = [0] * findNeededBitsToStoreInt(inputInt)
    
    for y in reversed(binaryPlaceValues):
        print(y)
        if int(y) > inputInt:
            print("Bit " + str(binaryPlaceValues.index(y)) + " Passing")
            pass
        else:
            print("Bit " + str(binaryPlaceValues.index(y)) + " Incrementing")
            bitsList[binaryPlaceValues.index(y)] = 1
            inputInt = inputInt - int(y)
            
    bitsListRev = list(reversed(bitsList))
    
    return bitsListRev


intToBeConverted = int(input("Enter Int: "))
print(convertIntToBits(intToBeConverted))


'''
    Note to Arion:
        We haven't yet done how to represent negative numbers in class, but effectively you use the first bit to represent positive [0] or negative [1] and then invert all the bits after
        so 5 ( [0,1,0,1] ) would become -5 ( [1,0,1,0] )
'''

'''
TODO:
    * Auto-scale bitsList size
    Error Handling
    Convert from Binary to Int
    Handle negative numbers
    Use bitLists properly
    * Auto calculate binary place values
    * Not have awful strings
'''
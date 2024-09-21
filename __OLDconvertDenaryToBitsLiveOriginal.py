def findLargestPowerOfTwo(inputInt: int):
    power = int(2)
    while power < inputInt:
       power = power * 2 
    
    return power
    
    
def convertIntToBits(inputInt: int):
    binaryPlaceValues = [1,2,4,8,16,32,64,128]
    bitsList = [0,0,0,0,0,0,0,0]
    IntToList = list(map(int,str(inputInt)))
    
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


intToBeConverted = int(input("Enter Int number: "))
print(convertIntToBits(intToBeConverted))

'''
TODO:
    Auto-scale bitsList size
    Error Handling
    Convert from Binary to Int
    Handle negative numbers
    Use bitLists properly
    Auto calculate binary place values
    * Not have awful strings
'''


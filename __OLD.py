'''

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


inputInt = int(input("What is your Int?: "))

print(findLargestPowerOfTwo(inputInt))


   

print("Start is 63, " + str(findLargestPowerOfTwo(63)))
print("Start is 64, " + str(findLargestPowerOfTwo(64)))
print("Start is 65, " + str(findLargestPowerOfTwo(65)))


print(findNeededBitsToStoreInt(int(0))) # 1
print(findNeededBitsToStoreInt(int(1))) # 1
print(findNeededBitsToStoreInt(int(2))) # 2
print(findNeededBitsToStoreInt(int(3))) # 2
print(findNeededBitsToStoreInt(int(4))) # 3


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
    
    
def convertIntToBits(inputInt: int):
    binaryPlaceValues = [1,2,4,8,16,32,64,128]
    bitsList = [0] * findNeededBitsToStoreInt(inputInt)
    IntToList = list(map(int,str(inputInt)))
    
    for x in enumerate(bitsList):
        print(x.type())
        x = int(x)
        print(x)
        binaryPlaceValue = binaryPlaceValues[x]
        print(binaryPlaceValue)
        
        if int(binaryPlaceValue) > inputInt:
            print("Bit " + str(bitsList.index(x)) + " Passing")
            pass
        else:
            print("Bit " + str(bitsList.index(x)) + " Incrementing")
            bitsList[bitsList.index(x)] = 1
            inputInt = inputInt - int(x)
        
    
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

def returnListOfPowersOf2(inputInt: int):
    powers = [1,2]
    power = int(1)
    
    while power < inputInt:
        power = power * 2
        if not power in powers:
            powers.append(power)
    return powers
            
print(returnListOfPowersOf2(128))
        
        

def findLargestPowerOfTwo(inputInt: int):
    power = int(2)
    while power < inputInt:
       power = power * 2 
    
    return power


# I know some inputs aren't validated properly and I'm overusing int() and str() but I've spent too long staring at TypeErrors and this fixes it
# Also mutating input arguments is bad form but I'm not sure of a nice way of tracking state that isn't just establishing an internal variable that mirrors the input

class binaryOperations:
    @staticmethod
    def findLargestPowerOfTwo(inputInt: int):
        power = int(2)
        while power < inputInt:
            power = power * 2 
        
        return power
    
    @staticmethod
    def findNeededBitsToStoreInt(inputInt: int):
        quantity = int(1)
        power = int(2)
        
        while power <= inputInt:
            power = power * 2
            quantity = quantity + 1
            
        return quantity
    
    @staticmethod
    def returnListOfPowersOf2(inputInt: int):
        powers = [1,2]
        power = int(1)
        
        while power < inputInt:
            power = power * 2
            if not power in powers:
                powers.append(power)
                
        return powers
        
    @staticmethod    
    def convertIntToBits(inputInt: int):
        binaryPlaceValues = binaryOperations.returnListOfPowersOf2(inputInt)
        bitsList = [0] * binaryOperations.findNeededBitsToStoreInt(inputInt)
        
        for y in reversed(binaryPlaceValues):
            # print(y)
            if int(y) > inputInt:
                # print("Bit " + str(binaryPlaceValues.index(y)) + " Passing")
                pass
            else:
                # print("Bit " + str(binaryPlaceValues.index(y)) + " Incrementing")
                bitsList[binaryPlaceValues.index(y)] = 1
                inputInt = inputInt - int(y)
                
        bitsListRev = list(reversed(bitsList))
        
        return bitsListRev
    
    @staticmethod
    def findBinaryPlaceValues(inputInt: int):
        """Returns a list containing ordered binary place values

        Args:
            inputInt (int): The amount of positions to return in the list

        Returns:
            list: List with binary place
        """
        binaryPlaceValues = []
        if inputInt:
            for i in range(inputInt):
                binaryPlaceValues.append(pow(2,i))
            return binaryPlaceValues
        else:
            return binaryPlaceValues

    @staticmethod
    def convertBinaryToInt(bitList: list):
        binaryPlaceValues = list(reversed(binaryOperations.findBinaryPlaceValues(len(bitList))))
        finalInt = 0
        for x in range(len(bitList)):
            if bitList[x] == 1:
                finalInt = finalInt + binaryPlaceValues[x]
            else:
                pass
        return finalInt
        


# intToBeConverted = int(input("Enter Int: "))
# print(binaryOperations.convertIntToBits(intToBeConverted))

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
# intToBeConverted = int(input("Enter Int: "))
# print(binaryOperations.convertIntToBits(intToBeConverted))
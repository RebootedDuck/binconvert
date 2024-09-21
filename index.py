import convertDenaryToBitsClass
'''
intToBeConverted = int(input("Enter Int: "))
print(convertDenaryToBitsClass.binaryOperations.convertIntToBits(intToBeConverted))
'''

with open('conversionChart.txt','w') as f:
    for i in range(0, 1025):
        f.write(str(i) + " - " + str(convertDenaryToBitsClass.binaryOperations.convertIntToBits(int(i))) + '\n')
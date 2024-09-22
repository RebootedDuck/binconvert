import os
import sys
import inspect
import unittest

currentDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentDir = os.path.dirname(currentDir)
sys.path.insert(0, parentDir) 

from binConvertClass import binaryOperations  # noqa: E402

testBits = [[[0],0],[[0,0,0],0],[[1,0,1],5],[[1,1,1],7],[[1,0,0,1],9],[[0,1,0,1,0,1,1],43]]

class testBinaryOperations(unittest.TestCase):
    def testConvertBitsToInt(self):
        trueness = True
        for index, item in enumerate(testBits):
            valueMatch = int(binaryOperations.convertBinaryToInt(testBits[index][0])) == int(testBits[index][1])
            if valueMatch:
                pass
            else:
                trueness= False
        self.assertTrue(trueness)
        
    def testConvertIntToBits(self):
        trueness = True
        for i in range(0,1000):
            bits = binaryOperations.convertIntToBits(i)
            convertedInt = binaryOperations.convertBinaryToInt(bits)
            
            if convertedInt == i:
                pass
            else:
                trueness = False
        self.assertTrue(trueness)
    
if __name__ == '__main__':
    unittest.main()
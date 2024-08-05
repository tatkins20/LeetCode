class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numEven = 0
        numDigitsList = []
        for num in nums:
            numDigits = 0
            if num == 0:
                numDigits = 1
            while num != 0:
                num = num/10
                numDigits += 1    
            numDigitsList.append(numDigits)
        print(numDigitsList)
        for num in numDigitsList:
            if num %2 == 0:
                numEven += 1
        return numEven

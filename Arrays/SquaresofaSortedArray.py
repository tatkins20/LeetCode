class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squared = [num**2 for num in nums]
        squared.sort()
        return squared

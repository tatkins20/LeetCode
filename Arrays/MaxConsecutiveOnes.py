class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxes = []
        con = 0
        for num in nums:
            if num: con+=1
            else:
                maxes.append(con)
                con = 0
        maxes.append(con)
        return max(maxes)

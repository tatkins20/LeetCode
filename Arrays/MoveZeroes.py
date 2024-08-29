class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_pter = 0
        for iter_pter in range(len(nums)):
            if nums[iter_pter] != 0 and nums[non_zero_pter] == 0:
                nums[iter_pter], nums[non_zero_pter] = nums[non_zero_pter], nums[iter_pter]
            if nums[non_zero_pter] != 0:
                non_zero_pter += 1

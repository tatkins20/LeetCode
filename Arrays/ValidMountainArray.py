class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        valley = 1
        length = len(arr)
        while valley < length and arr[valley] > arr[valley-1]:
            valley += 1
        
        if valley == 1 or valley == length:
            return False
        
        while length > valley and arr[valley] < arr[valley-1]:
            valley += 1
        
        return valley == length

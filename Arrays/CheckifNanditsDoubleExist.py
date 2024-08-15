class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            double = arr[i] * 2
            low, high = 0, len(arr)-1
            while low <= high:
                mid = (low+high)//2
                if arr[mid] == double and mid!= i:
                    return True
                elif arr[mid] < double:
                    low += 1
                else:
                    high -= 1
        return False

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        right_max = arr[length-1]
        arr[length-1] = -1
        for i in range(length-2, -1, -1):
            current = arr[i]
            arr[i] = right_max
            if right_max < current:
                right_max = current
        return arr

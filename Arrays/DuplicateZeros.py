class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        try: i = arr.index(0)
        except: return
        s = deque([0])
        for j in range(i+1, len(arr)):
            if arr[j] == 0:
                s.append(0)
                s.append(0)
            else:
                s.append(arr[j])
            arr[j] = s.popleft()

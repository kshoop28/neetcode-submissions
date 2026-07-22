class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1):
            if arr[i] == max(arr[i:]):
                arr[i] = max(arr[i+1:])
            else:
                arr[i] = max(arr[i:])
        arr[-1] = -1
        return arr
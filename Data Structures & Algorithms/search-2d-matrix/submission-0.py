class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lst = [item for sublist in matrix for item in sublist]

        left = 0
        right = len(lst) - 1

        while left <= right:
            middle = (left + right) // 2

            if lst[middle] == target:
                return True
            elif lst[middle] < target:
                left = middle + 1
            elif lst[middle] > target:
                right = middle - 1
                
        return False
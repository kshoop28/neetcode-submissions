class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0]) -1
        n = len(matrix[0])


        while left <= right:
            middle = (left + right) // 2
            row = middle // n
            col = middle % n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = middle + 1
            elif matrix[row][col]> target:
                right = middle - 1

        return False
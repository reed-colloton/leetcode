class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m - 1
        while l <= r:
            mid = (r + l) // 2
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][-1] < target:
                l = mid + 1
            else:
                row = mid
                l = 0
                r = n - 1
                while l <= r:
                    mid = (r + l) // 2
                    if matrix[row][mid] > target:
                        r = mid - 1
                    elif matrix[row][mid] < target:
                        l = mid + 1
                    else:
                        return True
        return False
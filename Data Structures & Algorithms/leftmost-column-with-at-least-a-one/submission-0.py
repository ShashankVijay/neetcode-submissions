# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # staircase: starting from [0, m - 1] top right cell
        # n: rows; m: cols
        # rows are sorted
        
        n, m = binaryMatrix.dimensions()
        currRow, currCol = 0, m - 1

        while currRow < n and currCol > -1:
            currCell = binaryMatrix.get(currRow, currCol)

            if currCell == 1:
                # move left in the same row
                currCol -= 1
            else:
                # either
                # we went through all 1s OR
                # row didn't have 1s
                # move to the next row, resume from (currRow + 1, currCol)
                currRow += 1

        if currCol == m - 1:
            # all 0s matrix
            return -1

        return currCol + 1
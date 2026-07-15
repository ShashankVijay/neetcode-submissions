class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        colMap = defaultdict(int)
        rowMap = defaultdict(int)

        m, n = len(picture), len(picture[0])
        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B":
                    colMap[j] += 1
                    rowMap[i] += 1

        res = 0
        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B" and colMap[j] == 1 and rowMap[i] == 1:
                    res += 1

        return res
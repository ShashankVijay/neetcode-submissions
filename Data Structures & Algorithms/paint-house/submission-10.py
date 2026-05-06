class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        table = [[0, 0, 0] for _ in range(n)]

        # first house
        table[0][0], table[0][1], table[0][2] = costs[0][0], costs[0][1], costs[0][2]

        for h in range(1, n):
            table[h][0] = costs[h][0] + min(table[h - 1][1], table[h - 1][2])
            table[h][1] = costs[h][1] + min(table[h - 1][0], table[h - 1][2])
            table[h][2] = costs[h][2] + min(table[h - 1][0], table[h - 1][1])

        return min(table[-1])

        

            
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        table = dict()

        def backtrack(i, r, b, g):
            # base cases
            if i == 0:
                if not r:
                    return min(costs[0][1], costs[0][2])
                elif not b:
                    return min(costs[0][0], costs[0][2])
                elif not g:
                    return min(costs[0][0], costs[0][1])
                else:
                    return min(costs[0][0], costs[0][1], costs[0][2])

            # memoization + computation
            c1, c2, c3 = float("inf"), float("inf"), float("inf")
            if r:
                if (i, "r") not in table:
                    table[(i, "r")] = c1 = costs[i][0] + backtrack(i - 1, False, True, True)
                else:
                    c1 = table[(i, "r")]
            if b:
                if (i, "b") not in table:
                    table[(i, "b")] = c2 = costs[i][1] + backtrack(i - 1, True, False, True)
                else:
                    c2 = table[(i, "b")]
            if g:
                if (i, "g") not in table:
                    table[(i, "g")] = c3 = costs[i][2] + backtrack(i - 1, True, True, False)
                else:
                    c3 = table[(i, "g")]

            return min(c1, c2, c3)

        return backtrack(n - 1, True, True, True)

            
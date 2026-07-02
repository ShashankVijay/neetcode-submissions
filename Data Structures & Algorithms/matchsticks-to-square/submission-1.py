class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # can sum of lengths be equally distributed
        # % 4 == 0?

        n = len(matchsticks)
        if sum(matchsticks) % 4 != 0:
            # a side length should be int
            return False

        # sqaure's each side is expected to be this
        sideLength = sum(matchsticks) // 4

        # so that we try out bigger sides first
        # rule them out quick if they don't fit
        matchsticks.sort(reverse = True)
        
        # try each matchstick in each of the 4 sides: 4 decisions every step
        sides = [0] * 4

        def backtrack(i):
            # i -> i'th matchstick
            if i >= n:
                return True

            for j in range(4):
                # for each side, try adding on a matchstick there
                if sides[j] + matchsticks[i] > sideLength:
                    continue

                # matchstick can be placed on this side: but is it the right side?
                # yes: return True
                # no: backtrack
                sides[j] += matchsticks[i] # ith placed; now recurse on remaining
                if backtrack(i + 1):
                    # if True is returned on remaining sticks, this combination worked
                    return True
                # current matchsticks[i] at sides[j]: didn't work
                # try matchsticks[i] on a different side
                sides[j] -= matchsticks[i]

            # if ith didn't go on any side well
            return False

        return backtrack(0)

            
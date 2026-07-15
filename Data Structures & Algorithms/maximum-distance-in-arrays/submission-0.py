class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = -float("inf")
        # running min max is the min max seen so far in subarrays up to i - 1
        # where i is the current index
        runningMin = min(arrays[0])
        runningMax = max(arrays[0])

        for i in range(1, len(arrays)):
            # max ith min ith is the current subarrays's max and min
            maxith = arrays[i][-1]
            minith = arrays[i][0]

            # we get the max distance using min and max combinations seen in 
            # subarrays up to i - 1 and at ith
            temp1 = abs(runningMax - minith)
            temp2 = abs(maxith - runningMin)

            # record the max in global max var res
            res = max(res, temp1, temp2)

            # update running min max taking ith into consideration
            # to maximise distance across all subarrays
            runningMax = max(maxith, runningMax)
            runningMin = min(minith, runningMin)

        return res
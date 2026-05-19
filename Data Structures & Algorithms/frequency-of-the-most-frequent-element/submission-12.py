class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        # window is valid? expand r
        # window is invalid? shrink l
        # validity: cost between l, r <= k
        # cost: operations between l, r needed to make them equal to nums[r]
        nums.sort()
        l = 0
        windowSum = 0
        maxFreq = -1
        for r in range(len(nums)):
            # cost to make nums[l]...nums[r - 1] = nums[r]
            windowSize = r - l + 1
            windowSum += nums[r]
            windowCost = (nums[r] * windowSize) - windowSum
            while windowCost > k:
                # as long as True: shrink [invalid window]
                windowSum -= nums[l]
                l += 1
                windowSize = r - l + 1
                windowCost = (nums[r] * windowSize) - windowSum
            # max of all valid windowSizes
            maxFreq = max(maxFreq, windowSize)

        return maxFreq

        
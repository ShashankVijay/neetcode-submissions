class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, 0
        k1 = k
        maxFreq = -1
        for r in range(len(nums)):
            # treating nums[r] as max so far
            m = nums[r]
            for i in range(r - 1, l - 1, -1):
                if k - (nums[r] - nums[i]) < 0:
                    l = i + 1
                    break
                k = k - (nums[r] - nums[i])
            k = k1
            maxFreq = max(maxFreq, r - l + 1)

        return maxFreq
        
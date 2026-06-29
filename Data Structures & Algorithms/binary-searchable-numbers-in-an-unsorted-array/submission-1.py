class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        # not guranteed to be found case for any nums[i]
        # [....pivot, ....., target] : target < pivot
        # [....target, ...., pivot] : target > pivot

        # COND 1: i.e for any nums[i] (i.e target to be found)
        # if any greater number comes before it, nums[i] will be evicted
        # so not all pivots guarantee nums[i] to be found

        # COND 2: similarly for any nums[i]
        # if any smaller number comes after it, nums[i] will be evicted again

        n = len(nums)

        leftMax = [0] * n
        leftMaxVal = -float("inf")

        rightMin = [0] * n
        rightMinVal = float("inf")

        # leftMax[i] = max value in 0...i
        for i in range(n):
            if nums[i] > leftMaxVal:
                leftMaxVal = nums[i]
            leftMax[i] = leftMaxVal

        # rightMin[i] = min value in i....n - 1
        for i in range(n - 1, -1, -1):
            if nums[i] < rightMinVal:
                rightMinVal = nums[i]
            rightMin[i] = rightMinVal

        res = 0
        for i in range(n):
            # if COND 1 or COND 2 is true, then nums[i] is not guranteed; skip
            if leftMax[i] > nums[i] or rightMin[i] < nums[i]:
                continue
            res += 1

        return res
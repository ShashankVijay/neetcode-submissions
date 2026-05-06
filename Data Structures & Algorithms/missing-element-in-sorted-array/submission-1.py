class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left < right:
            # mid = (left + right) // 2
            mid = right - (right - left) // 2
            # nums[0] to nums[mid]
            expectedPresence = nums[mid] - nums[0] + 1
            actualPresence = mid + 1
            missingBeforeMid = expectedPresence - actualPresence # (nums[mid]  - nums[0]) - mid 

            if missingBeforeMid < k:
                left = mid
            else:
                right = mid - 1

        m = nums[left] - nums[0] - left # missing count before nums[left], but still < k
        # need to advance by k - m more missing numbers after nums[left]
        answer = nums[left] + (k - m)

        return answer




            


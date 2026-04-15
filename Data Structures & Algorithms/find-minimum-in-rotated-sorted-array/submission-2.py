class Solution:
    def findMin(self, nums: List[int]) -> int:
        ## Solution 1: brute force - time O(n), space O(1)
        # linear search of array to find a minumum element
        # return min(nums)

        ## Solution 2: time O(log n), space O(1)
        # finding a lower bound
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]

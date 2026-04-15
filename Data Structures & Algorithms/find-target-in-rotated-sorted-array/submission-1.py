class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ## Solution 1: brute force - time O(n), space O(1)
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1

        ## Solution 2: time O(log n)
        # e.g: 4,5,6,7,0,1,2

        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
            
        pivot = l

        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        result = binary_search(0, pivot - 1)
        if result != -1:
            return result

        return binary_search(pivot, len(nums) - 1)
                
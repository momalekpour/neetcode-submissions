class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ## Solution 1: brute force - computing summation before and after each element using nested for loop
        # time complexity: O(n^2)
        # space complexity: O(1)

        ## Solution 2: finding intersection of presum and postsum arrays
        # time complexity: O(n)
        # space complexity: O(n)
        # e.g: array =   [1,7,3,6,5,6]
        #      prefix =  [0, 1, 8, 11, 17, 22]
        #      postfix = [27, 20, 17, 11, 6, 0]
        presum = [0] * len(nums)
        postsum = [0] * len(nums)

        # compute prefix sum array (sum of elements strictly to the left)
        for i in range(1, len(nums)):
            presum[i] = presum[i-1] + nums[i-1]
        
        # compute postfix sum array (sum of elements strictly to the right)
        for j in range(len(nums)-2, -1, -1):
            postsum[j] = postsum[j+1] + nums[j+1]
            
        # find leftmost pivot which is first common value index in 2 arrays
        for idx in range(len(nums)):
            if presum[idx] == postsum[idx]:
                return idx
        return -1
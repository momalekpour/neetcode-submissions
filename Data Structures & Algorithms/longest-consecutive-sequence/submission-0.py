class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ## Solution 1: brute force O(n^2) -> Time Limit Exceeded
        # res = 0
        # store = set(nums) 
        # for n in nums:
        #     curr, streak = n, 0
        #     while curr in store:
        #         streak += 1
        #         curr += 1
        #     res = max(res, streak)        
        # return res

        ## Solution 2: time and space O(n)
        res = 0
        store = set(nums)
        for n in nums:
            if (n-1) not in store:
                curr, streak = n, 0
                while curr in store:
                    streak += 1
                    curr += 1
                res = max(res, streak)
        return res

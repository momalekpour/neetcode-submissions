class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ## Solution 1: brute force O(n^3)
        triplets = set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if (i != j and i != k and j != k and
                        nums[i] + nums[j] + nums[k] == 0):
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        triplets.add(triplet)
        return [list(t) for t in triplets]

class Solution:
    def countElements(self, arr: List[int]) -> int:
        ## Solution 1: brute force - one pass iteration
        # time complexity: O(n^2)
        # space complexity: O( )

        res = 0
        for num in arr:
            if num + 1 in arr:
                res += 1
        return res
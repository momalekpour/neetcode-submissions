class Solution:
    def countElements(self, arr: List[int]) -> int:
        ## Solution 1: brute force - iterate on the arr + list lookup
        # time complexity: O(n^2)
        # space complexity: O(1)
        # res = 0
        # for num in arr:
        #     if num + 1 in arr:
        #         res += 1
        # return res

        ## Solution 2: hashmap - create freq hashmap and then do O(1) lookup
        # time complexity: O(n)
        # space complexity: O(n)
        freq_map = {}
        for n in arr:
            freq_map[n] = freq_map.get(n, 0) + 1

        res = 0
        for k in freq_map.keys():
            if k + 1 in freq_map:
                res += freq_map[k]
        return res



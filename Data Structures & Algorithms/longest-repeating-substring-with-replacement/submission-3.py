class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        ## Solution 2: sliding window - time O(m*n), space O(m)
        ##           l
        ## e.g: s = "ABAB", k = 2
        ##            r
        l = 0 
        chars = {}
        res = 0
        for r in range(len(s)):
            chars[s[r]] = chars.get(s[r], 0) + 1
            max_freq = max(chars.values())
            curr_len = r - l + 1
            if curr_len - max_freq <= k:
                res = max(res, curr_len)
            else:
                chars[s[l]] -= 1
                l += 1
        return res

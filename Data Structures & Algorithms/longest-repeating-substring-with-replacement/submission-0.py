class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ## Solution 1: brute force - time O(n^2)
        #           i
        # e.g: s = "ABAB", k = 2
        #            j
        
        res = 0
        for i in range(len(s)):
            chars = {}
            tmp = 0
            for j in range(i, len(s)):
                chars[s[j]] = chars.get(s[j], 0) + 1
                
                max_freq = max(chars.values())
                current_len = j - i + 1
                
                if current_len - max_freq <= k:
                    res = max(res, current_len)
                else:
                    break
        return res

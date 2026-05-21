class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_count_s = {}
        freq_count_t = {}
        for char in s:
            if char in freq_count_s:
                freq_count_s[char] +=1
            else:
                freq_count_s[char] = 1
        
        for char in t:
            if char in freq_count_t:
                freq_count_t[char] +=1
            else:
                freq_count_t[char] =1
        if freq_count_s == freq_count_t:
            return True
        else:
            return False

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        hash_set = set()
        max_len = 0
        while right < len(s):
            if s[right] not in hash_set:
                hash_set.add(s[right])
                right += 1
                max_len = max(max_len, len(hash_set))
            else:
                hash_set.remove(s[left])
                left += 1
        return max_len

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        seen = {}

        for right in range(len(s)):
            if s[right] in seen:
                if seen.get(s[right]) >= left:
                    left = seen.get(s[right])+1
            seen[s[right]] = right

            max_this_window = (right - left) + 1
            max_length = max(max_length, max_this_window)
        return max_length
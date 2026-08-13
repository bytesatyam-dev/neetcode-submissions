from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        
        need = Counter(t)
        window = {}
        have = 0
        need_count = len(need)

        left = 0
        best_len = float('inf')
        best_left = 0
        
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            
            if window[char] == need[char]:
                have += 1

            while have == need_count:
                window_len = right - left + 1
                if window_len < best_len:
                    best_len = window_len
                    best_left = left

                left_char = s[left]
                window[left_char] -= 1
                if window[left_char] < need[left_char]:
                    have -= 1
                left += 1

        return s[best_left:best_left+best_len] if best_len != float('inf') else ""
from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0
        max_freq = 0
        c = Counter()

        for i in range(len(s)):
            c[s[i]] += 1
            max_freq = max(max_freq, c[s[i]])

            window_size = i - left + 1
            if window_size - max_freq > k:
                c[s[left]] -= 1
                left += 1
                window_size -= 1

            max_length = max(max_length, window_size)

        return max_length
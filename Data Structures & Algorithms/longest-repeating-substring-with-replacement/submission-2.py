class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0
        max_freq = 0
        counts = [0] * 26

        for i in range(len(s)):
            idx = ord(s[i]) - ord('A')
            counts[idx] += 1
            max_freq = max(max_freq, counts[idx])

            window_size = i - left + 1
            if window_size - max_freq > k:
                left_idx = ord(s[left]) - ord('A')
                counts[left_idx] -= 1
                left += 1
                window_size -= 1

            max_length = max(max_length, window_size)

        return max_length
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

        for ch in s1:
            s1_count[ord(ch) - ord('a')] += 1
        for ch in s2[:len(s1)]:
            window_count[ord(ch) - ord('a')] += 1

        matches = sum(1 for i in range(26) if s1_count[i] == window_count[i])

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # character entering on the right
            enter_idx = ord(s2[right]) - ord('a')
            if window_count[enter_idx] == s1_count[enter_idx]:
                matches -= 1
            window_count[enter_idx] += 1
            if window_count[enter_idx] == s1_count[enter_idx]:
                matches += 1

            # character leaving on the left
            leave_idx = ord(s2[left]) - ord('a')
            if window_count[leave_idx] == s1_count[leave_idx]:
                matches -= 1
            window_count[leave_idx] -= 1
            if window_count[leave_idx] == s1_count[leave_idx]:
                matches += 1

            left += 1

        return matches == 26
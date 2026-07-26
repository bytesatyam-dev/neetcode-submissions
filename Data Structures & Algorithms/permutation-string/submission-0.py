from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter_obj = Counter(s1)
        check_window_len = len(s1)

        left = 0
        right = check_window_len
        if check_window_len <= len(s2):
            check_counter_obj = Counter(s2[left:right])
            if +check_counter_obj == s1_counter_obj:
                return True
            for i in range(len(s2)-right):
                check_counter_obj[s2[left]] -= 1
                check_counter_obj[s2[right]] += 1
                
                if +check_counter_obj == s1_counter_obj:
                    return True

                left += 1
                right += 1

        return False

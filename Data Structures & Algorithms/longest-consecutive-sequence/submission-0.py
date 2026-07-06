class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_streak = 0

        for num in nums_set:
            if (num - 1) not in nums_set:
                next_num = num
                current_length = 0
                while next_num in nums_set:
                    next_num += 1
                    current_length += 1
                longest_streak = max(longest_streak, current_length)

        return longest_streak
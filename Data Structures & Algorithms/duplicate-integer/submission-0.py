class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        is_duplicate = False
        for num in nums:
            if num in seen:
                is_duplicate = True
                break
            seen.add(num)
        return is_duplicate
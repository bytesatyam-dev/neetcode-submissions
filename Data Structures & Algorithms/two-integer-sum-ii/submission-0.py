class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = []

        len_nums = len(numbers)
        left = 0
        right = len_nums - 1
        while left < right:
            sum_nums = numbers[left] + numbers[right]

            if sum_nums == target:
                output = [left + 1, right + 1]
                break
            elif sum_nums < target:
                left += 1
            else:
                right -= 1
        return output


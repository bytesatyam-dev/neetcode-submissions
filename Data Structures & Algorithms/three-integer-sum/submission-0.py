class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        sorted_arr = sorted(nums)
        for i in range(len(nums)-2):
            if i > 0 and sorted_arr[i] == sorted_arr[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if sorted_arr[left]+sorted_arr[right] == -sorted_arr[i]:
                    output.append([sorted_arr[i],sorted_arr[left],sorted_arr[right]])
                    left += 1
                    right -= 1
                    while left < right and sorted_arr[left] == sorted_arr[left-1]:
                        left += 1
                    while left < right and sorted_arr[right] == sorted_arr[right+1]:
                        right -= 1
                elif sorted_arr[left]+sorted_arr[right] < -sorted_arr[i]:
                    left += 1
                elif sorted_arr[left]+sorted_arr[right] > -sorted_arr[i]:
                    right -= 1
        
        return output

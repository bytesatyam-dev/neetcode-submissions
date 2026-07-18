class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0]*len(height)
        max_right = [0]*len(height)

        result = []

        for i in range(len(height)):
            if i == 0:
                max_left[i] = height[i]
            else:
                max_left[i] = max(height[i], max_left[i-1])

        for j in range(len(height)-1,-1,-1):
            if j == len(height)-1:
                max_right[j] = height[j]
            else:
                max_right[j] = max(height[j], max_right[j+1])

        for k in range(len(height)):
            result.append(
                min(max_left[k], max_right[k]) - height[k]
            )

        return sum(result)
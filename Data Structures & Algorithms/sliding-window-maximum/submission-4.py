from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        dq = deque()  # stores indices, values in decreasing order front-to-back

        for right in range(len(nums)):
            # pop smaller values off the back — they're now useless
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()

            dq.append(right)

            # pop the front if it's fallen out of the window
            left = right - k + 1
            if dq[0] < left:
                dq.popleft()

            # window has fully formed — record the max
            if right >= k - 1:
                output.append(nums[dq[0]])

        return output
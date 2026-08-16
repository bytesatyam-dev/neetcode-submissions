from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        dq = deque()

        for p in range(len(nums)):
            # while looping i have to consider valid left & right pointer
            # also about deque, right side will be appended 
            # if we encounter something which is higher than dq[0] then remove
            # all first then add that pointer in dq
            # else <= then add in deque
            # but if dq which is deque of index and any index is not of current 
            # window remove it

            left_point = right_point = None
            if k > 1 and p >= k-1:
                left_point = p+1-k
                right_point = p
            elif k == 1:
                left_point = right_point = p
            elif k == 0:
                return output

            while dq and nums[p] >= nums[dq[-1]]:
                dq.pop()

            dq.append(p)

            if isinstance(left_point, int) and left_point >= 0:
                while dq and dq[0] < left_point:
                    dq.popleft()


            if isinstance(left_point, int) and left_point >= 0:
                output.append(nums[dq[0]])

        return output
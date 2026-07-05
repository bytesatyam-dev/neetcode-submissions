from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_obj = Counter(nums)
        # space complexity = O(n) ; time complexity = O(nlogn)
        counter_obj_sorted = sorted(list(counter_obj.items()), key = lambda x:x[1], reverse=True)

        # space complexity = O(k) ; time complexity = O(k)
        output = []
        for i, (a, b) in enumerate(counter_obj_sorted):
            if i < k:
                output.append(a)
            continue
        return output

        # resultant will be # space complexity = O(n + k) ; time complexity = O(nlogn + k)

    
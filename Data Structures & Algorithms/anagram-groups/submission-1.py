from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_dict = defaultdict(list)
        for sstr in strs: # O(n) as going through each item
            key = tuple(sorted(sstr)) # O(klog(k)) for sorted method
            anagram_dict[key].append(sstr)
        
        return list(anagram_dict.values())
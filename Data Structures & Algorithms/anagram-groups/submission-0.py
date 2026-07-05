class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter, defaultdict

        anagram_dict = defaultdict(list)
        for sstr in strs:
            key = tuple(sorted(sstr))
            anagram_dict[key].append(sstr)
        
        return list(anagram_dict.values())
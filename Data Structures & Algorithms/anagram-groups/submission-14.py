class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for s in strs:
            sortedS = ''.join(sorted(s))
            anagram_dict[sortedS].append(s)

        return list(anagram_dict.values())
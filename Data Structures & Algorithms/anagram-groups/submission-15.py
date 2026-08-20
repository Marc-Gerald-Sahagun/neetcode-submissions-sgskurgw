class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_dict = {}
        for s in strs:
            sortedS = sorted(s)
            sortedS = ''.join(sortedS)
            
            if sortedS not in anagram_dict:
                anagram_dict[sortedS] = []
                
            anagram_dict[sortedS].append(s)


        return list(anagram_dict.values())


        
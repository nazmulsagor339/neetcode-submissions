class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for i in strs:
            sorted_str = ''.join(sorted(i)) # sorting each word
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str].append(i)
            else:
                anagram_dict[sorted_str] = []
                anagram_dict[sorted_str].append(i)
        anagram_list = [anagram_dict[i] for i in anagram_dict]
        return anagram_list
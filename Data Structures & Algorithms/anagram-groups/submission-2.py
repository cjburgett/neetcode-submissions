class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Technically Big O stays stable but bunch of loops
        maps = dict()

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in maps:
                # scenario the word is in maps already
                maps[sorted_word].append(word)
            else:
                maps[sorted_word] = [word]
            
        answer = list(maps.values())
        return answer


        
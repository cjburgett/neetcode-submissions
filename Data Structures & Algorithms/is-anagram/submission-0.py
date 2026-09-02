class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # can do this by sorting the string turn into an array then sort and compare
        # can also do this by creating a dictionary and adding to see if equal
        s1 = ''.join(sorted(s))
        t1 = ''.join(sorted(t))
        return t1 == s1
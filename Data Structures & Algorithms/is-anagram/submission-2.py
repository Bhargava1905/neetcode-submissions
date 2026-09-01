class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = list(s)
        list2 = list(t)
        if len(list1) != len(list2):
            return False
        return sorted(list1) == sorted(list2)
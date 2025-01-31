class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        list_s = s.split(' ')
        return len(list_s[-1])

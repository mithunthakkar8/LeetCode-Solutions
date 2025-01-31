import re
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        found = re.search(needle,haystack)
        return found.start() if found else -1

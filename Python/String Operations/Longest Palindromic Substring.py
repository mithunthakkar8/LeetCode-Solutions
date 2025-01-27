class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ''
        # Iterate over each character of string
        for i, char in enumerate(s):
            # Generate substrings iteratively with longest first
            for j in range(len(s[i:]),0,-1):
                substring = s[i:i+j]
                # if substring is a palindrome and if it is longer than the last longest 
                # palindrome, make that substring the longest_palindrome
                if substring == substring[::-1] and len(substring)>len(longest_palindrome):
                    longest_palindrome=substring
                    break
        return longest_palindrome
        

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ''
        longest_substring = ''
        candidates_lengths = [len(longest_substring)]
        candidates = [longest_substring]
        for i in s:
            if i in substring:
                substring = substring[substring.rfind(i)+1:]
            substring = substring + i
            if len(substring)>=candidates_lengths[-1]:
                candidates_lengths[-1]=len(substring)
                candidates[-1] = substring
            else:
                candidates_lengths.append(len(substring))
                candidates.append(substring)
            print(substring)
        print(candidates)

        return max(candidates_lengths)


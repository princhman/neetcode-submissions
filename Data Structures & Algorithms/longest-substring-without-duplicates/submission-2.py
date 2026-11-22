class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        longest = 1
        i = 1
        current = s[0]
        while i < len(s):
            if s[i] in current:
                # reset to character after other s[i]
                # if current = "xyzb" and there is another y, 
                # shift got to be -2 
                # find is 1
                # len is 4
                longest = max(longest, len(current))
                shift_left = (1 + current.find(s[i])) - len(current)
                current = s[i] if shift_left == 0 else current[shift_left:] + s[i]
            else:
                current += s[i]
            i+=1
        longest = max(longest, len(current))
        return longest

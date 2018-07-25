class Solution:
    def longestPalindrome(self, s):
        max_len = 0
        left_index = 0
        right_index = 0
        for i in range(len(s)):
            j = 1
            str_len = 1
            while i - j >= 0 and i + j <= len(s) - 1:
                if s[i - j] == s[i + j]:
                    str_len += 2
                    if str_len > max_len:
                        left_index = i - j
                        right_index = i + j
                        max_len = str_len
                    j += 1
                else:
                    break
        for i in range(len(s)):
            j = 1
            str_len = 2
            while i - j >= 0 and i + j + 1 <= len(s) - 1:
                if s[i] == s[i + 1]:
                    if s[i - j] == s[i + j + 1]:
                        str_len += 2
                        if str_len > max_len:
                            left_index = i - j
                            right_index = i + 1 + j
                            max_len = str_len
                        j += 1
                    else:
                        break

        return s[left_index:right_index+1]


s = Solution()
print(s.longestPalindrome("abba"))
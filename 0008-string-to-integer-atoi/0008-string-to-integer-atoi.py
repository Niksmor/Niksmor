import re
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s):
            if not s[0].isalpha():
                i = re.search(r"^(-\d+)|^(\+\d+)|^(\d+)",s)
                if i is not None:
                    i = int(i.group())
                    if i < 0:
                        return max(-2**31, i)
                    return min(2**31 - 1, i)
        return 0
        
class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        new_string = ""
        sum = 0
        p = len(s)-1
        while p >= 0:
            value = (sum + ord(s[p]) + shifts[p] - 97)%26 + 97
            # new_string.insert(0, chr(value)) works for arrays
            new_string = chr(value) + new_string
            sum += shifts[p]
            p -= 1

        return new_string
        
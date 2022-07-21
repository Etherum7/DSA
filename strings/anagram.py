

class Solution:

    # Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self, a, b):
        # code here
        n = len(a)
        m = len(b)
        if n != m:
            return False
        d = {}
        for c in a:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
            cnt = len(d)
        for c in b:
            if c not in d:
                return False
            d[c] -= 1
            if d[c] < 0:
                return False
            elif d[c] == 0:
                cnt -= 1
        if cnt == 0:
            return True

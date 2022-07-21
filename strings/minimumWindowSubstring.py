# User function Template for python3

class Solution:

    # Function to find the smallest window in the string s consisting
    # of all the characters of string p.
    def smallestWindow(self, s, p):
        # code here
        cmap = {}
        for c in p:
            if c in cmap:
                cmap[c] += 1
            else:
                cmap[c] = 1
        # print(cmap)
        i = j = 0
        N = len(s)
        mn = N+1

        start = 0
        cnt = len(cmap)

        if len(p) > N:
            return -1
        while j < N:
            # print(cmap)

            if s[j] in cmap:
                cmap[s[j]] -= 1
                if cmap[s[j]] == 0:
                    cnt -= 1
                while cnt == 0:
                    if mn > j-i+1:
                        mn = j-i+1
                        start = i

                    if s[i] in cmap:
                        cmap[s[i]] += 1
                        if cmap[s[i]] > 0:
                            cnt += 1
                    i += 1
            j += 1

        return -1 if mn > N else s[start:start+mn]

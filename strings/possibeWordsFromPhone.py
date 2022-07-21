class Solution:

    # Function to find list of all words possible by pressing given numbers.
    def possibleWords(self, a, N):
        # Your code here
        d = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']
             }
        res = []

        def util(pos, ans):
            if len(ans) == N:
                res.append(ans)
                return
            value = d[a[pos]]
            for key in value:
                util(pos+1, ans+key)
        util(0, '')
        return res

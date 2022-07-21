class Solution:
    def isRepeat(self, s):
        # code here
        S = s+s
        S = S[1:-1]
        if S.find(s) != -1:
            return 1
        else:
            return 0


class Solution:
    def isRepeat(self, s):
        # code here
        total = {}
        if len(s) <= 1:
            return 0

        for c in s:
            if c not in total:
                total[c] = 1

            else:
                total[c] += 1
        if len(total) == 1:
            return 1
        print(total)

        # for value in total.values():
        #     if value % 2 == 1:
        #         return 0
        repeat = ''
        d = {}
        for c in s:
            repeat += c
            if not c in d:
                d[c] = 1
            else:
                d[c] += 1
            total[c] -= 1
            if len(d) == len(total):
                flag = 1
                for key in total.keys():
                    if total[key] == 0:
                        return 0
                    if total[key] % d[key] != 0:
                        flag = 0
                        break
                if flag == 1:
                    break
        print(repeat)
        t = ''
        while len(t) < len(s):
            t += repeat
            print(t)
            if t == s:
                return 1
        return 0


ob = Solution()
# print(ob.isRepeat('ababab'))
# print(ob.isRepeat('ababac'))
print(ob.isRepeat('jccjccjcc'))

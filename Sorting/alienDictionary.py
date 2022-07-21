class Solution:
    def util(self, a, b, order):
        if not a or not b:
            return
        if a[0] != b[0]:
            # store order
            print(f'{a[0]} greater than {b[0]} ')
            if a[0] in order and b[0] in order:
                order[a[0]] = order[b[0]]-1

            elif a[0] in order and not b[0] in order:
                order[b[0]] = order[a[0]]+1

            elif not a[0] in order and b[0] in order:
                order[a[0]] = order[b[0]]-1

            elif not a[0] in order and not b[0] in order:
                order[a[0]] = 1
                order[b[0]] = 2
                pass

            return
        else:
            self.util(a[1:], b[1:], order)

    def findOrder(self, d, N, K):
        order = {}
        for i in range(0, N-1):
            self.util(d[i], d[i+1], order)
        res= [t[0] for t in sorted(list(order.items()), key=lambda x: x[1])]
        return ''.join(res)


ob = Solution()
print(ob.findOrder(["baa", "abcd", "abca", "cab", "cad"], 5, 4))
print(ob.findOrder(["caa","aaa","aab"], 3, 3))

from itertools import zip_longest
# class Solution:
#     def compareVersion(self, version1: str, version2: str) -> int:
#         v1=map(int, version1.split('.'))
#         v2=map(int, version2.split('.'))
#         for rev1,rev2 in zip_longest(v1,v2, fillvalue=0):
#             if rev1>rev2:
#                 return 1
#             elif rev1<rev2:
#                 return -1
#         return 0


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def parse(ver: str) -> List[int]:
            return [int(k) for k in ver.split('.')]

        v1, v2 = parse(version1), parse(version2)
        i = 0
        print(v1, v2)
        while i < len(v1) or i < len(v2):
            a = v1[i] if i < len(v1) else 0
            b = v2[i] if i < len(v2) else 0
            if a < b:
                return -1
            elif a > b:
                return 1
            i += 1
        return 0

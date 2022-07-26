class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        numbers = []
        for i in range(1, n):
            fact = fact*i
            numbers.append(i)
        numbers.append(n)
        k -= 1
        ans = ''
        while True:
            ans = ans+str(numbers[k//fact])
            # print(k,fact, 2//2)
            numbers.pop(k//fact)
            if len(numbers) == 0:
                return ans
            k = k % fact
            fact = fact//len(numbers)


# # include <bits/stdc++.h>

# using namespace std


# class Solution {
#     public:
#     // function to generate all possible permutations of a string
#     void solve(string & s, int index, vector < string > & res) {
#         if (index == s.size()) {
#             res.push_back(s)
#             return
#         }
#         for (int i=index
#              i < s.size()
#              i++) {
#             swap(s[i], s[index])
#             solve(s, index + 1, res)
#             swap(s[i], s[index])
#         }
#     }

#     string getPermutation(int n, int k) {
#         string s
#         vector < string > res
#         // create string
#         for (int i=1
#              i <= n
#              i++) {
#             s.push_back(i + '0')
#         }
#         solve(s, 0, res)
#         // sort the generated permutations
#         sort(res.begin(), res.end())
#         // make k 0-based indexed to point to kth sequence
#         auto it = res.begin() + (k - 1)
#         return *it
#     }
# }


# int main() {
#     int n = 3, k = 3
#     Solution obj
#     string ans = obj.getPermutation(n, k)
#     cout << "The Kth permutation sequence is " << ans << endl

#     return 0
# }

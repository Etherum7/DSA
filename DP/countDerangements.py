""" 
    Time complexity: O(2 ^ N)
    Space complexity: O(N)

    Where 'N' is the number of elements.
"""

from sys import stdin, setrecursionlimit
import sys
setrecursionlimit(10**6)

MOD = 1000000007

def countDerangements(n):
    # Base conditions.
    if n == 1:
        return 0

    if n == 2:
        return 1

    # Recurse for other subproblems.
    return ((n - 1) % MOD * (countDerangements(n - 1) % MOD + countDerangements(n - 2) % MOD) % MOD) % MOD

# Main
t = int(input())
while t:
    n = int(input())
    print(countDerangements(n))
    t = t-1
# # Memeoized array
# string='nitin'
# class Solution1:
#     def __init__(self):
#         self.t=[[-1]*(len(string)+1) for j in range(len(string)+1)]
#     def isPalindrome(self,s):
#         return s==s[::-1]
#     def util(self, string, i, j):
#         if (i>=j):
#             return 0
#         if self.t[i][j]!=-1:
#             return self.t[i][j]
#         if (self.isPalindrome(string[i:j+1])):

#             return 0
#         self.t[i][j]= float('inf')
#         for k in range(i, j):
#             self.t[i][j]= min(self.t[i][j], 1+self.util(string, i, k)+self.util(string, k+1, j))
#         return self.t[i][j]

#     def palindromicPartition(self, string):

#         j=len(string)
#         return self.util(string, 0, j-1)
# memo dict
class Solution2:
    def __init__(self):
        self.memo = {}

    def convert(self, a, b):
        return str(a)+str(b)

    def isPali(self, s):
        return s == s[::-1]

    def util(self, s, i, j):
        if i > j:
            return 0
        ij = self.convert(i, j)
        if ij in self.memo:
            return self.memo[ij]
        if i == j:
            self.memo[ij] = 0
            return 0
        if self.isPali(s[i:j+1]):
            self.memo[ij] = 0
            return 0
        MIN = 100000000
        for k in range(i, j):
            leftMin = rightMin = 100000000
            leftKey = self.convert(i, k)
            rightKey = self.convert(k+1, j)

            if leftKey in self.memo:
                leftMin = self.memo[leftKey]
            if rightKey in self.memo:
                rightMin = self.memo[rightKey]
            if leftMin == 100000000:
                leftMin = self.util(s, i, k)
                self.memo[leftKey] = leftMin
            if rightMin == 100000000:
                rightMin = self.util(s, k+1, j)
                self.memo[rightKey] = rightMin
            MIN = min(MIN,leftMin+rightMin+1)
            
            self.memo[ij] = MIN
        return self.memo[ij]

    def palindromicPartition(self, string):
        n = len(string)-1
        return self.util(string, 0, n)
# accepted

def minCut(a):
 
    cut = [0 for i in range(len(a))]
    palindrome = [[False for i in range(len(a))] for j in range(len(a))]
    for i in range(len(a)):
        minCut = i;
        for j in range(i + 1):
            if (a[i] == a[j] and (i - j < 2 or palindrome[j + 1][i - 1])):      
                palindrome[j][i] = True;
                minCut = min(minCut,0 if  j == 0 else (cut[j - 1] + 1));
        cut[i] = minCut;  
    return cut[len(a) - 1];
# parent
# Dynamic Programming Solution for
# Palindrome Partitioning Problem

# Returns the minimum number of
# cuts needed to partition a string
# such that every part is a palindrome
def minPalPartion(str):
	
	# Get the length of the string
	n = len(str)
	
	# Create two arrays to build the
	# solution in bottom up manner
	# C[i][j] = Minimum number of cuts
	# needed for palindrome
	# partitioning of substring str[i..j]
	# P[i][j] = true if substring str[i..j]
	# is palindrome, else false. Note that
	# C[i][j] is 0 if P[i][j] is true
	C = [[0 for i in range(n)]
			for i in range(n)]
	P = [[False for i in range(n)]
				for i in range(n)]

	# different looping variables
	j = 0
	k = 0
	L = 0
	
	# Every substring of length
	# 1 is a palindrome
	for i in range(n):
		P[i][i] = True;
		C[i][i] = 0;
		
	# L is substring length. Build the
	# solution in bottom-up manner by
	# considering all substrings of
	# length starting from 2 to n.
	# The loop structure is the same as
	# Matrix Chain Multiplication problem
	# (See https://www.geeksforgeeks.org / matrix-chain-multiplication-dp-8/ )
	for L in range(2, n + 1):
		
		# For substring of length L, set
		# different possible starting indexes
		for i in range(n - L + 1):
			j = i + L - 1 # Set ending index
			
			# If L is 2, then we just need to
			# compare two characters. Else
			# need to check two corner characters
			# and value of P[i + 1][j-1]
			if L == 2:
				P[i][j] = (str[i] == str[j])
			else:
				P[i][j] = ((str[i] == str[j]) and
							P[i + 1][j - 1])
							
			# IF str[i..j] is palindrome,
			# then C[i][j] is 0
			if P[i][j] == True:
				C[i][j] = 0
			else:
				
				# Make a cut at every possible
				# location starting from i to j,
				# and get the minimum cost cut.
				C[i][j] = 100000000
				for k in range(i, j):
					C[i][j] = min (C[i][j], C[i][k] +
								C[k + 1][j] + 1)
									
	# Return the min cut value for
	# complete string. i.e., str[0..n-1]
	return C[0][n - 1]

# Driver code
str = "ababbbabbababa"
print ('Min cuts needed for Palindrome Partitioning is',
									minPalPartion(str))
									
# This code is contributed
# by Sahil shelangia

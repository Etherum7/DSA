class Solution:
	def hasArrayTwoCandidates(self,arr, n, x):
		# code here
		d={}
		for i in arr:
		    if  x-i in d:
		        return True
		    if not i in d:
		        d[i]=1
		return False
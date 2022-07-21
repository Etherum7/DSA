class Solution():
    def minSprinkler(self, arr, N):
        #your code goes here
        cover=[]
        for index, val in enumerate(arr):
            s=set()
            for i in range(max(index+1-val, 1), min(index+1+val, N)+1):
                s.add(i)
            cover.append(s)
        print(cover)
        res=1
        pos=set([i for i in range(1,N+1)])
        cover.sort(key=lambda x : len(x), reverse=True)
        pos= pos-cover[0]
        print(pos)
        if len(pos)==0:
            return res
        while len(pos):
            minLength=float('inf')
            n=set()
            for c in cover[1:]:
                if len(pos-c)<minLength:
                    n=pos-c
                    minLength = len(pos-c)
            
            pos=n
            print(pos)
            res+=1
        return res
# ob=Solution()
# print(ob.minSprinkler([3,0,3,0,3,3,0,3,3], 9))

# # Python program for the above approach

# Function to find minimum number of
# sprinkler to be turned on
def minSprinklers(arr, N):

	# Stores the leftmost and rightmost
	# point of every sprinklers
	V = [];
	
	# Traverse the array arr[]
	for i in range(N):
		if (arr[i] > -1):
			V.append([i - arr[i], i + arr[i]]);
		
	# Sort the array sprinklers in
	# ascending order by first element
	V.sort();

	# Stores the rightmost range
	# of a sprinkler
	maxRight = 0;
	
	# Stores minimum sprinklers
	# to be turned on
	res = 0;

	i = 0;

	# Iterate until maxRight is
	# less than N
	while (maxRight < N):

		# If i is equal to V.size()
		# or V[i][0] is greater
		# than maxRight

		if (i == len(V) or V[i][0] > maxRight):
			return -1;
	
		# Stores the rightmost boundary
		# of current sprinkler
		currMax = V[i][1];

		# Iterate until i+1 is less
		# than V.size() and V[i+1][0]
		# is less than or equal to maxRight
		while (i + 1 < len(V) and V[i + 1][0] <= maxRight):

			# Increment i by 1
			i += 1;
			# Update currMax
			currMax = max(currMax, V[i][1]);


		# If currMax is less than the maxRight
		if (currMax < maxRight):
			# Return -1
			return -1;

		# Increment res by 1
		res += 1;

		# Update maxRight
		maxRight = currMax + 1;

		# Increment i by 1
		i += 1;
	# Return res as answer
	return res;


# Drive code.

# Input
# arr = [-1, 2, 2, -1, 0, 0];
# N = len(arr);

# Function call
print(minSprinklers([3,0,3,0,3,3,0,3,3], 9))

# This code is contributed by _saurabh_jaiswal.
# minSprinklers(arr, N)
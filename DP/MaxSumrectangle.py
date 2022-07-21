class Solution:
    def kadane(self, temp, R):
        max_sum_till_now = -99999999999
        s = 0
        for i in range(R):
            s += temp[i]
            if max_sum_till_now < s:
                max_sum_till_now = s
            if s < 0:
                s = 0
        if max_sum_till_now != -99999999999:
            return max_sum_till_now
        max_sum_till_now = temp[0]

        # Find the maximum element in array
        for i in range(1, R):
            if temp[i] > max_sum_till_now:
                max_sum_till_now = temp[i]

        return max_sum_till_now

    def maximumSumRectangle(self, R, C, M):
        # code here
        maxSum = -999999999999

        for left in range(C):
            temp = [0]*R
            for right in range(left, C):
                for i in range(R):
                    temp[i] += M[i][right]
                    S = self.kadane(temp, R)
                    if S > maxSum:
                        maxSum = S
        return S
# Python3 program to find maximum sum
# subarray in a given 2D array

# Implementation of Kadane's algorithm
# for 1D array. The function returns the
# maximum sum and stores starting and
# ending indexes of the maximum sum subarray
# at addresses pointed by start and finish
# pointers respectively.


def kadane(arr, n):

	# initialize sum, maxSum and
	Sum = 0
	maxSum = -999999999999
	i = None
	for i in range(n):
		Sum += arr[i]
		if Sum < 0:
			Sum = 0
		elif Sum > maxSum:
			maxSum = Sum
	if maxSum != -999999999999:
		return maxSum

	maxSum = arr[0]
	for i in range(1, n):
		if arr[i] > maxSum:
			maxSum = arr[i]
	return maxSum


def findMaxSum(M):
	global ROW, COL

	maxSum = -999999999999

	temp = [None] * ROW
	Sum = 0
	for left in range(COL):
		temp = [0] * ROW
		for right in range(left, COL):
			for i in range(ROW):
				temp[i] += M[i][right]
			Sum = kadane(temp, ROW)
			if Sum > maxSum:
				maxSum = Sum

    return maxSum




# from typing import List


# def prev_permutation(A:List[int])->List[int]:
#     inversion_point=len(A)-2
#     while inversion_point >= 0 and A[inversion_point]<=A[len(A)-1]:
#         inversion_point-=1
#     if(inversion_point==-1):
#         return []
#     # swap
#     A[inversion_point], A[len(A)-1] = A[len(A)-1] , A[inversion_point] 
#     A[inversion_point+1:] = sorted(A[inversion_point+1:], reverse=True)

#     return A
# # print(prev_permutation([6,2,1,0,3,4,5]))
# # print(prev_permutation([7,9,6]))
# # print(prev_permutation([1,2,3]))
# # print(prev_permutation([7,4,6]))
# print(prev_permutation([1,1,2,3]))
# print(prev_permutation([1,1,3,2]))
# print(prev_permutation([1,2,1,3]))
# print(prev_permutation([1,2,3,1]))

# Python 3 program to
# print all permutations with
# duplicates allowed
# using prev_permutation()

# Function to compute the
# previous permutation


def prevPermutation(str):

	# Find index of the last element
	# of the string
	n = len(str) - 1

	# Find largest index i such that
	# str[i - 1] > str[i]
	i = n
	while (i > 0 and str[i - 1] <= str[i]):
		i -= 1

	# if string is sorted in ascending order
	# we're at the last permutation
	if (i <= 0):
		return False

	# Note - str[i..n] is sorted in
	# ascending order

	# Find rightmost element's index
	# that is less than str[i - 1]
	j = i - 1
	while (j + 1 <= n and
		str[j + 1] <= str[i - 1]):
		j += 1

	# Swap character at i-1 with j
	str = list(str)
	temp = str[i - 1]
	str[i - 1] = str[j]
	str[j] = temp
	str = ''.join(str)

	# Reverse the substring [i..n]
	str[::-1]

	return True, str


# Driver code
if __name__ == '__main__':
	str = "1213"

	b, str = prevPermutation(str)

	if (b == True):
		print("Previous permutation is", str)
	else:
		print("Previous permutation doesn't exist")

# This code is contributed by
# Sanjit_Prasad

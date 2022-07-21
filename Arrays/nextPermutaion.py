def nextPermutation(nums):
    n= len(nums)
    # find the point where inc sub sequence ends 
    # from that find an element just greater then that 
    # next to that sort 
    i=n-2
    while nums[i]>=nums[i+1]:
        i-=1
    k=i
    for j in range(i+1,n):
        if(nums[j]> nums[i]):
            k=j
            break
    nums[k], nums[i]=nums[i],nums[k]
    # nums[i+1:].sor
    nums[i+1:]=sorted(nums[i+1:])
    return nums


print(nextPermutation([1,2,3]))
print(nextPermutation([4,9,7,8]))
print(nextPermutation([4,9,9,3]))
print(nextPermutation([1,2,3]))


# class Solution {
# public:
#     void nextPermutation(vector<int>& nums) {
#         int n = nums.size(), k, l;
#     	for (k = n - 2; k >= 0; k--) {
#             if (nums[k] < nums[k + 1]) {
#                 break;
#             }
#         }
#     	if (k < 0) {
#     	    reverse(nums.begin(), nums.end());
#     	} else {
#     	    for (l = n - 1; l > k; l--) {
#                 if (nums[l] > nums[k]) {
#                     break;
#                 }
#             } 
#     	    swap(nums[k], nums[l]);
#     	    reverse(nums.begin() + k + 1, nums.end());
#         }
#     }
# };





# def optimalMergePattern(arr ,n):
#     # array of arrays 
#     sorted_arr=sorted(arr, key=lambda x :len(x))
#     res=[len(i) for i in sorted_arr] 
#     print(sorted_arr, res)


    
# optimalMergePattern([[3,8,12,20,24,25],[5,9,11,16]],2)
def optimalMergePattern(arr):
    sorted_arr= sorted(arr)
    res=[]
    for _ in range(len(arr)-1):
        sum_arr= sorted_arr[0] + sorted_arr[1]
        sorted_arr=sorted([sum_arr]+sorted_arr[2:])
        
        res.append(sum_arr)
        
    print(sum(res))
    print(res)
    
    
optimalMergePattern([20,30,10,5,30])


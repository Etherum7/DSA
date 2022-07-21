def jobSequencingwithDeadlines(arr, t):
    result=[False]*t
    job=['-1']*t
    n= len(arr)

    # sort in decreasing order of profit
    arr= sorted(arr, key=lambda x: x[2],reverse=True)
    print(arr)
    for i in range(n):
        for j in range(min(t-1, arr[i][1]-1), -1, -1):
            # print(j)
            if(not result[j]):
                result[j] = True
                job[j]=arr[i][0]
                break
    print(job)
            


    # print(arr)

    pass
arr = [['a', 2, 100],  # Job Array
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 1, 25],
       ['e', 3, 15]]
jobSequencingwithDeadlines(arr,3)
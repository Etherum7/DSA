// {Driver Code Starts
    # include<bits/stdc++.h>
    using namespace std

    // } Driver Code Ends


class Solution{

    public:
    int transfigure(string A, string B)
    {
        // Your code goes here
        int n = A.size()
        int m = B.size()
        if (n != m)return -1
        int count[256] = {0}
        for(int i=0
            i < n
            i++){
            count[A[i]] += 1
            count[B[i]] -= 1
        }
        for(int i=0
            i < n
            i++){
            if (count[A[i]]){
                return -1
            }
        }
        int i = n-1, j = i, ans = 0
        while (i >= 0){
            if(A[i] == B[j]){
                j -= 1
            }
            else{
                ans += 1
            }
            i -= 1
        }
        return ans
    }
}


// {Driver Code Starts.


    int main()
    {
        int t
        cin >> t
        while (t--)
        {
            string A, B
            cin >> A >> B
            Solution obj
            cout << obj.transfigure(A, B) << endl
        }
    }  // } Driver Code Ends

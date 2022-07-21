// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
//User function template for C++
class Solution{
public:
     int first(vector<int> &mat, int low, int high){
         while (low<=high){
             int mid=low+(high-low)/2;
             if((mid==0 or mat[mid-1]==0) and mat[mid]==1){
                 return mid;
             }
             else if(mat[mid]==0){
                 return first(mat, mid+1, high);
             }
             else{
                 return first(mat,low, mid-1);
             }
         }
     }
	int rowWithMax1s(vector<vector<int> > arr, int n, int m) {
	    // code here
	    int row=0;
	    int maxi=0;
	    for(int i=0; i<n;i++){
	       // int j=0;
	        if (arr[i][m-1]==0){
	            continue;
	        }
	       // while (arr[i][j]==0){
	       //     j+=1;
	       // }
	        int j=first(arr[i], 0, m-1);
	        if(m-j>maxi){
	            maxi=m-j;
	            row=i;
	            if(maxi==m){
	                return i;
	            }
	        }
	       
	        
	    }
	    if(maxi==0) return -1;
	    return row;
	}

};

// { Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        vector< vector<int> > arr(n,vector<int>(m));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin>>arr[i][j];
            }
        }
        Solution ob;
        auto ans = ob.rowWithMax1s(arr, n, m);
        cout << ans << "\n";
    }
    return 0;
}
  // } Driver Code Ends
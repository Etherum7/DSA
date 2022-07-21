#include <bits/stdc++.h>
using namespace std;

int main()
{
    
    return 0;
}
class Solution
{
public:
    int getMinDiff(int arr[], int n, int k)
    {
        // code here
        sort(arr, arr + n);
        int tempMin = arr[0];
        int tempMax = arr[n - 1];
        int ans = tempMax - tempMin;
        for (int i = 1; i < n; i++)
        {
            if (arr[i] - k < 0)
                continue;
            tempMin = min(arr[0] + k, arr[i] - k);
            tempMax = max(arr[i - 1] + k, arr[n - 1] - k);
            ans = min(ans, tempMax - tempMin);
        }
        return ans;
    }
};

class Solution{   
public:
    int getMinDiff(int arr[], int n, int k) {
        // code here
        sort(arr, arr+n);
        int tempMin= arr[0];
        int tempMax=arr[n-1];
        int ans = tempMax-tempMin;
        for(int i=1; i <n;i++){
            tempMin= min(arr[0]+k, arr[i]-k);
            tempMax=max(arr[i-1]+k, arr[n-1]-k);
            ans= min(ans,tempMax-tempMin);
        }
        return ans;
    }
};

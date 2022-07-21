#include <bits/stdc++.h>
using namespace std;

int main()
{

    return 0;
}
long long int findMaxSum(vector<int> &arr, int n)
{
    // code here

    long long int prev2 = arr[0];
    if (n == 1)
    {
        return prev2;
    }

    long long int prev1 = max(arr[0], arr[1]);
    for (int i = 2; i < n; i++)
    {
        long long int curi = max(prev2 + arr[i], prev1);
        prev2 = prev1;

        prev1 = curi;
    }
    return prev1;
}
long long int houseRobber(vector<int> &valueInHouse)
{
    // Write your code here.
    vector<int> temp1, temp2;
    int n = valueInHouse.size();
    if (n == 1)
        return valueInHouse[0];
    for (int i = 0; i < n; i++)
    {
        if (i != 0)
            temp1.push_back(valueInHouse[i]);
        if (i != n - 1)
            temp2.push_back(valueInHouse[i]);
    }
    return max(findMaxSum(temp1, n - 1), findMaxSum(temp2, n - 1));
}

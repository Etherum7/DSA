// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{
public:
    // Function to return a list of integers denoting spiral traversal of matrix.
    vector<int> spirallyTraverse(vector<vector<int>> matrix, int r, int c)
    {
        // code here
        int total = r * c;
        int count = 0;
        int startingRow = 0;
        int startingCol = 0;
        int endingRow = r - 1;
        int endingCol = c - 1;

        vector<int> ans;
        while (count < total)
        {
            for (int k = startingCol; k <= endingCol and count < total; k++)
            {
                ans.push_back(matrix[startingRow][k]);
                count += 1;
            }
            startingRow += 1;
            for (int k = startingRow; k <= endingRow and count < total; k++)
            {
                ans.push_back(matrix[k][endingCol]);
                count += 1;
            }
            endingCol -= 1;
            for (int k = endingCol; k >= startingCol and count < total; k--)
            {
                ans.push_back(matrix[endingRow][k]);
                count += 1;
            }
            endingRow -= 1;
            for (int k = endingRow; k >= startingRow and count < total; k--)
            {
                ans.push_back(matrix[k][startingCol]);
                count += 1;
            }
            startingCol += 1;
        }
        return ans;
    }
};
// { Driver Code Starts.

// { Driver Code Starts.
int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int r, c;
        cin >> r >> c;
        vector<vector<int>> matrix(r);

        for (int i = 0; i < r; i++)
        {
            matrix[i].assign(c, 0);
            for (int j = 0; j < c; j++)
            {
                cin >> matrix[i][j];
            }
        }

        Solution ob;
        vector<int> result = ob.spirallyTraverse(matrix, r, c);
        for (int i = 0; i < result.size(); ++i)
            cout << result[i] << " ";
        cout << endl;
    }
    return 0;
} // } Driver Code Ends
// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

/* Link list node */
struct Node
{
    int data;
    Node *next;

    Node(int x)
    {
        data = x;
        next = NULL;
    }
};

void push(struct Node **head_ref, int new_data)
{

    struct Node *new_node = new Node(new_data);

    new_node->next = (*head_ref);
    (*head_ref) = new_node;
}

int countTriplets(struct Node *head, int x);

/* Driver program to test count function*/
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, x, i, num;
        struct Node *head = NULL;
        cin >> n >> x;
        for (i = 0; i < n; i++)
        {
            cin >> num;
            push(&head, num);
        }

        /* Check the count function */
        cout << countTriplets(head, x) << endl;
    }
    return 0;
} // } Driver Code Ends

// User function Template for C++

int countTriplets(struct Node *head, int x)
{
    // code here.
    vector<int> arr;
    Node *p = head;
    while (p)
    {
        arr.push_back(p->data);
        p = p->next;
    }
    int order = 0;
    int n = arr.size();
    if (arr[0] < arr.back())
    {
        order = 1;
    }
    int cnt = 0;
    for (int i = 0; i < n; i++)
    {
        int j = i + 1;
        int k = n - 1;
        int target = x - arr[i];
        // cout<<x<<' '<< arr[i]<<' '<<target<<' ';
        while (j < k)
        {
            int actual = arr[j] + arr[k];

            if (actual == target)
            {
                cnt += 1;
                // cout<<actual<<' '<<i<<' '<<j<<' '<<k<<' ';
                j += 1;
                k -= 1;
            }
            else if (actual < target)
            {
                if (order)
                    j += 1;
                else
                    k -= 1;
            }
            else
            {
                if (order)
                    k -= 1;
                else
                    j += 1;
            }
        }
    }
    return cnt;
}
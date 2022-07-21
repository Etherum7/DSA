#include <bits/stdc++.h>
using namespace std;
struct Node
{
    Node *links[2];

    bool containsKey(int ind)
    {
        return (links[ind] != NULL);
    }
    Node *get(int ind)
    {
        return links[ind];
    }
    void put(int ind, Node *node)
    {
        links[ind] = node;
    }
};
class Trie
{
private:
    Node *root;

public:
    Trie()
    {
        root = new Node();
    }

public:
    void insert(int num)
    {
        Node *node = root;
        // cout << num << endl;
        for (int i = 31; i >= 0; i--)
        {
            int bit = (num >> i) & 1;
            if (!node->containsKey(bit))
            {
                node->put(bit, new Node());
            }
            node = node->get(bit);
        }
    }

public:
    int findMax(int num)
    {
        Node *node = root;
        int maxNum = 0;
        for (int i = 31; i >= 0; i--)
        {
            int bit = (num >> i) & 1;
            if (node->containsKey(!bit))
            {
                maxNum = maxNum | (1 << i);
                node = node->get(!bit);
            }
            else
            {
                node = node->get(bit);
            }
        }
        return maxNum;
    }
};
vector<int> maxXorQueries(vector<int> &arr, vector<vector<int>> &queries)
{
    //	Write your coode here.
    sort(arr.begin(), arr.end());
    vector<pair<int, pair<int, int>>> offlineQueries;
    int n = queries.size();
    for (int i = 0; i < n; i++)
    {
        offlineQueries.push_back({queries[i][1], {queries[i][0], i}});
    }
    sort(offlineQueries.begin(), offlineQueries.end());
    int index = 0;
    vector<int> ans(n, 0);
    int m = arr.size();
    Trie trie;
    for (auto &it : offlineQueries)
    {

        while (index < m and arr[index] <= it.first)
        {
            trie.insert(arr[index]);
            index += 1;
        }
        if (index == 0)
        {
            ans[it.second.second] = -1;
        }
        else
        {
            ans[it.second.second] = trie.findMax(it.second.first);
        }
    }
    return ans;
}
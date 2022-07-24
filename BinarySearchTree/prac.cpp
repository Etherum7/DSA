#include <bits/stdc++.h>
using namespace std;

int main()
{
    
    return 0;
}
class Solution {
public:
    TreeNode * solve(vector<int>& preorder, int mini, int maxi, int &i){
        if(i>=preorder.size()) return NULL;
        if(preorder[i]>mini and preorder[i]<maxi){
            TreeNode * node = new TreeNode(preorder[i]);
            i+=1;
            node->left=solve(preorder, mini,node->val , i);
            node->right=solve(preorder, node->val,maxi, i);
            return node;
}
        return NULL;      
    }
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        int i=0;
        return solve(preorder, 0, 1001, i);
    }
};
class Solution
{
public:
    Node *connect(Node *root)
    {
        if (!root)
            return root;
        queue<pair<Node *, int>> q;
        q.push({root, 0});
        while (q.size())
        {
            pair<Node *, int> temp = q.front();
            q.pop();
            if (q.size() && q.front().second == temp.second)
            {
                temp.first->next = q.front().first;
            }
            else
            {
                temp.first->next = NULL;
            }
            if (temp.first->left)
            {
                q.push({temp.first->left, temp.second + 1});
            }
            if (temp.first->right)
            {
                q.push({temp.first->right, temp.second + 1});
            }
        }
        return root;
    }
};

class Solution {
public:
    bool inorder(TreeNode* root, int k,unordered_set<int> &s){
        if (!root){
            return false;
        }
        if(inorder(root->left, k, s)) return true;
        if(s.find(k-root->val)!=s.end()) return true;
        s.insert(root->val);
        if(inorder(root->right, k, s)) return true;
        return false;
        
    }
    bool findTarget(TreeNode* root, int k) {
        unordered_set<int> s;
        return inorder(root, k, s);
        
    }
};

class info{
public:
    int mini;
    int maxi;
    bool isBST;
    int sum;
};
class Solution {
public:
    info solve(TreeNode* root, int &ans){
        // base case
        if (root==NULL){
            return {INT_MAX,INT_MIN,true,0};
        }
        
        info left=solve(root->left,ans);
        info right = solve(root->right,ans);
        
        info curr;
        
        curr.sum = left.sum + right.sum + root->val;
        curr.mini = min(root->val,left.mini);
        curr.maxi = max(root->val,right.maxi);
        if(left.isBST and right.isBST and (left.maxi < root->val) and (right.mini > root->val)){
            curr.isBST = true;
        }
        else{
            curr.isBST = false;
        }
        
        if(curr.isBST){
            ans = max(ans,curr.sum);
        }
        return curr;
          
    }
    int maxSumBST(TreeNode* root) {
        int  maxSum=0;
        solve(root,maxSum);
        return maxSum;
    }
};
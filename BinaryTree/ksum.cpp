/*************************************************************
    
    Following is the Binary Tree node structure.
    
    class BinaryTreeNode {
        public : 
            T data;
            BinaryTreeNode<T> *left;
            BinaryTreeNode<T> *right;
    
            BinaryTreeNode(T data) {
                this -> data = data;
                left = NULL;
                right = NULL;
            }
    };
    
*************************************************************/
void path(BinaryTreeNode<int> *root, int k, vector<vector<int>> &res , vector<int>&op){
    if (root){
        op.push_back(root->data);
        
        path(root->left, k, res, op);
        
        path(root->right, k,  res, op);
        
//         sum terminating at this
        int n= op.size();
        int sum=0;
        for(int i=n-1; i>=0;i--){
            sum+=op[i];
            if (sum==k){
                res.push_back({op.begin()+i,op.end()});
                
}
            
        }
        op.pop_back();
        
    }
    
}
vector<vector<int>> kPathSum(BinaryTreeNode<int> *root, int k) {
    // Write your code here.
    vector<vector<int>> res;
    vector<int>op;
    path(root, k,  res, op);
    return res;
    
}

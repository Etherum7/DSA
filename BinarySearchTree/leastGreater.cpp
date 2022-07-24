//{ Driver Code Starts
/* Driver program to test above function */

#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//Back-end complete function Template for C++
class Node{
    public:
    int data;
        Node* left;
        Node*right;
    Node(int d){
        this->data=d;
        this->left=NULL;
        this->right=NULL;
    }
};

class Solution{
    void insert(Node *root, int key){
        Node *t = NULL;
        while(root){
            t=root;
            if(root->data==key){
                return;
            }
            else if(root->data>key){
                root=root->left;
            }
            else{
                root=root->right;
            }
        }
        if(t->data>key){
            t->left=new Node(key);
        }
        else{
            t->right=new Node(key);
        }
        return;
    
        
    }
    Node * search(Node * root, int elem){
        Node * res=NULL;
        while (root){
            
            if(root->data>elem){
                res=root;
                root=root->left;
            }
            else{
                root=root->right;
            }
        }
        return res;
    }
    public:
    
    vector<int> findLeastGreater(vector<int>& arr, int n) {
        Node * root=new Node(arr[n-1]);
        vector<int> res(n, -1);
        for(int i=n-2; i>=0;i--){
            Node * pos=search(root, arr[i]);
            if(pos){
                res[i]=pos->data;
            }
            insert(root, arr[i]);
            
        }
        return res;
    }
};

//{ Driver Code Starts.
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin >> n;
	    vector<int>arr(n);
	    for(int i = 0 ; i < n; i++){
	        cin >> arr[i];
	    }
	    Solution ob;
	    vector<int> ans = ob.findLeastGreater(arr, n);
	    for(auto it : ans){
	        cout << it << " ";
	    }
	    cout <<endl;
	}
	return 0;
}

// } Driver Code Ends
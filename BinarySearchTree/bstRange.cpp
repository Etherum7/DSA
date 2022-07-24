// # Function to count number of nodes in BST that lie in the given range.
// # class Solution:
// #     def preorder(self, root, low, high, cnt):
// #         if root:
// #             if low <= root.data <= high:
// #                 cnt[0] += 1
// #             if low <= root.data:
// #                 self.preorder(root.left, low, high, cnt)
// #             if high >= root.data:
// #                 self.preorder(root.right, low, high, cnt)

// #     def getCount(self, root, low, high):
// #         # Your code here
// #         cnt = [0]
// #         self.preorder(root, low, high, cnt)
// #         return cnt[0]

//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

struct Node
{
	int data;
	Node *left;
	Node *right;
	// Node(int d)
	// {
	// 	data = d;
	// 	left = NULL;
	// 	right = NULL;
	// }
};
// Utility function to create a new Tree Node
Node *newNode(int val)
{
	Node *temp = new Node;
	temp->data = val;
	temp->left = NULL;
	temp->right = NULL;

	return temp;
}
// Function to Build Tree
Node *buildTree(string str)
{
	// Corner Case
	if (str.length() == 0 || str[0] == 'N')
		return NULL;

	// Creating vector of strings from input
	// string after spliting by space
	vector<string> ip;

	istringstream iss(str);
	for (string str; iss >> str;)
		ip.push_back(str);

	// Create the root of the tree
	Node *root = newNode(stoi(ip[0]));

	// Push the root to the queue
	queue<Node *> queue;
	queue.push(root);

	// Starting from the second element
	int i = 1;
	while (!queue.empty() && i < ip.size())
	{

		// Get and remove the front of the queue
		Node *currNode = queue.front();
		queue.pop();

		// Get the current node's value from the string
		string currVal = ip[i];

		// If the left child is not null
		if (currVal != "N")
		{

			// Create the left child for the current node
			currNode->left = newNode(stoi(currVal));

			// Push it to the queue
			queue.push(currNode->left);
		}

		// For the right child
		i++;
		if (i >= ip.size())
			break;
		currVal = ip[i];

		// If the right child is not null
		if (currVal != "N")
		{

			// Create the right child for the current node
			currNode->right = newNode(stoi(currVal));

			// Push it to the queue
			queue.push(currNode->right);
		}
		i++;
	}

	return root;
}

// } Driver Code Ends
// Function to count number of nodes in BST that lie in the given range.
class Solution
{
public:
	int getCount(Node *root, int l, int h)
	{
		// your code goes here
		if (!root)
			return 0;
		int count = 0;
		int curr = root->data;
		if (curr >= l and curr <= h)
			count = 1;
		if (curr < l)
		{
			return getCount(root->right, l, h);
		}
		if (curr > h)
		{
			return getCount(root->left, l, h);
		}
		return getCount(root->left, l, h) + getCount(root->right, l, h) + count;
	}
};

//{ Driver Code Starts.

int main()
{

	int t;
	scanf("%d ", &t);
	while (t--)
	{
		string s;
		getline(cin >> ws, s);
		int l, r;
		cin >> l >> r;
		Solution ob;
		Node *root = buildTree(s);
		cout << ob.getCount(root, l, r) << endl;
	}
	return 1;
}

// } Driver Code Ends
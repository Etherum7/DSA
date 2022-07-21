#    node *next[26]={NULL};
# };
# /*You are required to complete this method */
# int func(node *root,string &s,int j){
#    node *head=root;int c=0;
#    for(int i=j;i<s.size();i++){
#        if(!head->next[s[i]-'a']){
#            c++;
#            head->next[s[i]-'a']=new node;
#        }
#        head=head->next[s[i]-'a'];
#    }
#    return c;
# }
# int countDistinctSubstring(string s)
# {
#    //Your code here
#    node *root=new node;int c=0;
#    for(int i=0;i<s.size();i++) c+=func(root,s,i);
#    return c+1;
# }

# User function Template for python3
class Node:
    def __init__(self):
        self.links = [None]*26

    def containsKey(self, ch):
        return self.links[ord(ch)-ord('a')] != None

    def put(self, ch, node):
        self.links[ord(ch)-ord('a')] = node

    def get(self, ch):
        return self.links[ord(ch)-ord('a')]


def countDistinctSubstring(s):
    # code here
    cnt = 0
    root = Node()

    n = len(s)
    for i in range(n):
        node = root
        for ch in s[i:]:
            if not node.containsKey(ch):
                node.put(ch, Node())
                cnt += 1
            node = node.get(ch)

    return cnt+1


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        print(countDistinctSubstring(s))
# } Driver Code Ends

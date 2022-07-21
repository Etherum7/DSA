class Solution:

    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    def maximumMeetings(self, n, start, end):
        # code here
        meetings = [(i, start[i], end[i]) for i in range(n)]
        meetings.sort(key=lambda x: x[2])
        res = []
        cnt = 0
        last = (-1, 0, 0)
        for meeting in meetings:
            if meeting[1] > last[2]:
                cnt += 1
                last = meeting
        return cnt
# // { Driver Code Starts
# //Initial Template for C++

# #include <bits/stdc++.h>
# using namespace std;


#  // } Driver Code Ends
# //User function Template for C++

# class Solution{

# static bool comp(pair<int, pair<int, int>> p1, pair<int, pair<int, int>> p2){
#     if(p1.first==p2.first){
#         return p1.second.second<p2.second.second;
#     }
#     return p1.first<p2.first;
# }
# public:
#     vector<int> maxMeetings(int N,vector<int> &S,vector<int> &F){
#         vector<pair<int, pair<int, int>>> schedule;
#         for(int i=0; i<N;i++){
#             pair<int, pair<int, int>> p={F[i],{S[i], i+1}};
#             schedule.push_back(p);
#         }
#         sort(schedule.begin(),schedule.end(), comp);
#         vector<int> res;
#         int finish=INT_MIN;
#         for(auto it: schedule){
#             if(it.second.first>finish){
#                 res.push_back(it.second.second);
#                 finish=it.first;
#             }
#         }
#         sort(res.begin(), res.end());
#         return res;
        
#     }
# };

# // { Driver Code Starts.

# int main(){
#     int t;
#     cin>>t;
#     while(t--){
#         int n;
#         cin>>n;
#         vector<int> S(n),F(n);
#         for(int i=0;i<n;i++){
#             cin>>S[i];
#         }
#         for(int i=0;i<n;i++){
#             cin>>F[i];
#         }
#         Solution ob;
#         vector<int> ans=ob.maxMeetings(n,S,F);
#         for(int i=0;i<ans.size();i++){
#             cout<<ans[i];
#             if(i!=ans.size()-1){
#                 cout<<" ";
#             }
#         }
#         cout<<endl;
#     }
#     return 0;
# }  // } Driver Code Ends
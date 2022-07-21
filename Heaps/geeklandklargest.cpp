#include <bits/stdc++.h>
using namespace std;


class Solution {
public:
    long long colosseum(int N,vector<int> A) {

       
      priority_queue<long long,vector<long long>,greater<long long>> pq;
      vector<long long>prefMax;
      long long sum = A[0];
      pq.push(A[0]);
      for(int i=1;i<2*N;i++)
      {
         if(pq.size() < N) {
             sum+=A[i];
             pq.push(A[i]);
         }
         else if(pq.size() == N && pq.top() < A[i]) {
             sum-=pq.top();
             pq.pop();
             pq.push(A[i]);
             sum+=A[i];
         }
         
         if(pq.size() == N) {
             prefMax.push_back(sum);
         }
         
      }
      
      vector<long long> suffixMin;
      sum = A[3*N-1];
      priority_queue<long long > pq2;
      pq2.push(sum);
      for(int i=3*N-2;i >= N;i--)
      {
         if(pq2.size() < N) {
             sum+=A[i];
             pq2.push(A[i]);
         }
         else if(pq2.size() == N && pq2.top() > A[i]) {
             sum-=pq2.top();
             pq2.pop();
             pq2.push(A[i]);
             sum+=A[i];
         }
         if(pq2.size() == N) {
             suffixMin.push_back(sum);
         }
         
      }
      
      long long ans = INT_MIN;
      int prefixIndex = 0;
      int suffixIndex = suffixMin.size()-1;
      while(prefixIndex < prefMax.size() && suffixIndex >= 0)
      {
          long long curr_ans = prefMax[prefixIndex]-suffixMin[suffixIndex];
          ans = max(ans,curr_ans);
          prefixIndex++;
          suffixIndex--;
      }
      
      return ans;
    
   
   }
};
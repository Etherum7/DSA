#include <bits/stdc++.h>
using namespace std;


int main(){
    vector<int> qry;
    
    int count=0;
    cin>>count;
    while(count--){
        int x;
        cin>>x;
        qry.push_back(x);

    };
    for(auto it: qry){
        cout<<it<<' ';
    }
    return 0;
}
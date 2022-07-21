#include <bits/stdc++.h>
using namespace std;

int main()
{

    return 0;
}
vector<int> adj[n + 1], vis(n + 1, 0), level(n + 1, 0), euler;
for (int i = 0; i < edge.size(); i++)
{
    int u = edge[i][0], v = edge[i][1];
    adj[u].push_back(v);
    adj[v].push_back(u);
}
sol(0, 0, vis, level, euler, adj);
map<int, pair<int, int>> mp;
int m = euler.size();
for (int i = 0; i < m; i++)
{
    if (mp.find(euler[i]) == mp.end())
    {
        mp[euler[i]].first = i;
    }
    mp[euler[i]].second = i;
}
vector<int> pre(m, 0), suff(m, 0);
pre[0] = level[euler[0]];
suff[m - 1] = level[euler[m - 1]];
for (int i = 1; i < m; i++)
{
    pre[i] = max(pre[i - 1], level[euler[i]]);
}
for (int i = m - 2; i >= 0; i--)
{
    suff[i] = max(suff[i + 1], level[euler[i]]);
}
vector<int> a;
for (int i = 0; i < q; i++)
{
    int u = que[i][0], v = que[i][1];
    int ind = (level[u] > level[v] ? u : v);
    int s = mp[ind].first, e = mp[ind].second;
    int ans = max(pre[s - 1], suff[e + 1]);
    a.push_back(ans);
}
return a;
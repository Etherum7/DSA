#include <bits/stdc++.h>
using namespace std;

int main()
{
    string s1 = "Hello, world!";
    string s2;
    s2 = s1.substr(0, 3);
    s1.erase(1, 3);
    cout << s2 << ' ' << s1;
    vector<int> v = {1, 2, 3, 4, 5};
    v.insert(v.begin() + 2, 6);
    for (auto it : v)
    {
        cout << it;
    }
    return 0;
}
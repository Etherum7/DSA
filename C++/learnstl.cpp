#include <bits/stdc++.h>
// #include <math.h>
using namespace std;
// std::cin
void print()
{
    cout << "raj";
}
int sum(int a, int b)
{
    return a * b;
}
void explainPairs()
{
    pair<int, int> p = {1, 2};
    cout << p.first << " " << p.second << endl;
    pair<int, pair<int, int>> p1 = {2, {3, 4}};
    cout << p1.first << ' ' << ' ' << p1.second.first << ' ' << p1.second.second << endl;
    pair<int, int> arr[] = {p, {4, 5}};
    for (auto it : arr)
    {
        cout << it.first << " " << it.second << endl;
    }
}
void explainVector()
{
    vector<int> v;
    v.push_back(23);
    v.emplace_back(45);
    vector<pair<int, int>> vec;
    vec.push_back({1, 2});
    // assumes pair
    vec.emplace_back(8, 0);
    // pre filed
    // [100]*5
    vector<int> v(5, 100);
    // garbage
    vector<int> v(5);

    // copy vector into
    vector<int> v2(v);

    vector<int> v1 = {10, 20, 30, 50, 40};
    cout << v1[2] << endl;
    cout << v1.back() << endl;

    vector<int>::iterator it = v1.begin();
    cout << *(it) << endl;
    it += 1;
    cout << *(it) << endl;

    vector<int>::iterator it1 = v.end();
    // end points to last+1
    // use it-=1
    for (vector<int>::iterator it = v.begin(); it != v.end(); it++)
    {
        cout << *(it) << endl;
    }
    for (auto it = v.begin(); it != v.end(); it++)
    {
        cout << *(it) << endl;
    }
    for (auto it : v)
    {
        cout << it << ' ';
    }

    v1.erase(v1.begin() + 2);
    for (auto it : v1)
    {
        cout << it << ' ';
    }

    // Insert
    v.insert(v.begin(), 300);
    // Inset 2 times
    v.insert(v.begin() + 1, 3, 5);

    v.insert(v.begin(), v1.begin(), v1.begin() + 3);

    // size
    cout << v.size();

    v.pop_back();

    v1.swap(v2);

    v.clear();

    cout << v.empty();
}
// fromt operations dll=list
// vector single linked list
void explainList()
{
    list<int> ls;

    ls.push_back(9);
    ls.emplace_back(89);

    ls.push_front(56);
    ls.emplace_front(78);
}

void explainDeque()
{
    deque<int> dq;
    // similar fn
    dq.back();
    dq.front();
    
}
void explainStack()
{
    stack<int> st;
    st.push(1);
    st.push(2);
    st.push(3);
    st.push(4);

    st.emplace(6);

    cout << st.top();
    st.pop();

    cout << st.size();
    cout << st.empty();

    stack<int> st1, st2;
    st1.swap(st2);
}
void explainQueue()
{
    queue<int> q;
    q.push(1);
    q.push(2);
    q.push(3);
    q.push(4);
    q.back() += 5;
    // back is 4+5
    cout << q.back();
    cout << q.front();
    q.pop();
}

void explainPQ()
{
    // max heap
    priority_queue<int> pq;
    pq.push(8);
    pq.push(10);
    pq.push(1);
    pq.push(109);

    cout << pq.top();
    // print 109

    pq.pop();
    cout << pq.top();

    // Minimum heap
    priority_queue<int, vector<int>, greater<int>> pq;
priority_queue<int, vector<int>, greater<vector<int>>> pq;
    pq.push(1);
    pq.push(6);
    cout << pq.top();
}

void explainSet()
{
    // sorted and unique
    set<int> st;
    st.insert(1);
    st.insert(2);
    st.emplace(3);
    st.insert(3);
    
    // {1,2,3,4}
    // Not linear
    // returns an iterator that points to 3
    auto it = st.find(3);
    auto it = st.find(6);
    // not here therefore return st.end()
    st.erase(2);
    // Ologn
    int cnt = st.count(1);
    // cnt only 1 or 0
    auto it = st.find(3);
    st.erase(it);
    st.erase(st.find(2), st.find(3));

    auto it = st.lower_bound(2);
    auto it = st.upper_bound(3);
    cout<<"here";
    cout<<*(it);
    // log time
    // as bst
}

void explainMultiSet()
{
    multiset<int> ms;
    // sorted not unique
    ms.insert(1);
    ms.insert(1);
    ms.insert(1);
    // all erase
    ms.erase(1);
    int cnt = ms.count(1);
    ms.erase(ms.find(1));
}

void explainUnorderedSet()
{
    // unique not sorted
    unordered_set<int> st;
    // O(1) insertion
    // no lower and upper
    st.insert(1);
    // erase in 1
    // worst case
    // o(N)
}
void explainMap()
{
    // logn
    map<int, int> mpp;
    map<int, pair<int, int>> mpp2;
    map<pair<int, int>, int> mpp3;

    // keys can be unique but
    // map stores unique keys in sorted order
    mpp[1] = 2;
    mpp.emplace(1, 2);
    mpp.insert(2, 3);
    

    mpp3[{2, 3}] = 10;
    for (auto it : mpp)
    {
        cout << it.first << endl;
        cout << it.second << endl;
    }
    // if not exist gives zero
    cout << mpp[5];

    auto it = mpp.find(3);
    // cout << *(it);

    auto it = mpp.find(5);
    // not find at end;
}

void explainMultiMap()
{
    // duplicate key
    // no mpp[key]
}
void explainUnorderedMap()
{
    // randomized sorted
    // 1 to n worst case
}

bool comp(pair<int, int> p1, pair<int, int> p2)
{
    // assume first is correct
    if (p1.second < p2.second)
        return true;
    if (p1.second > p2.second)
        return false;

    if (p1.first > p2.first)
        return true;
    return false;
}
void algo()
{
    int a[] = {5, 4, 3, 2, 1};
    int n = sizeof(a) / sizeof(a[0]);
    sort(a, a + n);
    // start and ending iterator
    for (auto it : a)
    {
        cout << it;
    }
    vector<int> v = {1, 2, 3};
    sort(v.begin(), v.end());
    sort(a + 2, a + 4);
    // descending
    // greater comparator
    // sort(a, a + n, greater<int>);

    pair<int, int> a[] = {{1, 2}, {3, 1}, {5, 1}};
    // 5,3,1

    sort(a, a + n, comp);

    int num = 7;
    int cnt = __builtin_popcount(num);
    // tellse 3 one in num set bits
    long long num = 167783297823987;
    int cnt = __builtin_popcountll(num);
    string s = "123";
    sort(s.begin(), s.end());
    do
    {
        cout << s << endl;
    } while (next_permutation(s.begin(), s.end()));
    // int maxi = max_element(v.begin(), v.end());
}

int main()
{
    print();
    cout << sum(4, 5) << endl;
    explainPairs();
    return 0;
}
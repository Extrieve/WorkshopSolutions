#include <bits/stdc++.h>
 
using namespace std;
 
int main() {
	int n;
    cin >> n;
    vector<int> vec(n);
    for(auto& i : vec)
        cin >> i;
    sort(vec.begin(), vec.end());
    int q;
    cin >> q;
    for(int i = 0; i < q; ++i) {
        int a;
        cin >> a;
        cout << upper_bound(vec.begin(), vec.end(), a)- vec.begin() << '\n';
    }
    return 0;
}
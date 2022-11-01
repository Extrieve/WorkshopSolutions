#include <bits/stdc++.h>
 
using namespace std;
 
int main() {
	int n, q;
    cin >> n >> q;
    vector<int> vec(n);
    for(auto& i : vec)
        cin >> i;
    for(int i = 0; i < q; ++i) {
        int a;
        cin >> a;
        int it = upper_bound(vec.begin(), vec.end(), a) - vec.begin();
		cout << it << '\n';
    }
    return 0;
}
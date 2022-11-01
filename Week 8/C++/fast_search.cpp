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
        int left_val, right_val;
		cin >> left_val >> right_val;
		auto left_it = lower_bound(vec.begin(), vec.end(), left_val);
		auto right_it = upper_bound(vec.begin(), vec.end(), right_val);
		cout << right_it - left_it << ' ';
    }
    return 0;
}
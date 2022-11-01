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
        if(binary_search(vec.begin(), vec.end(), a)) {
			cout << "YES\n";
		}
		else {
			cout << "NO\n";
		}
    }
    return 0;
}
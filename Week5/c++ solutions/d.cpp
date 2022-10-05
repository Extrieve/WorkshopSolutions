#include <iostream>
#include <set>
 
using namespace std;
 
int main() {
  	int n;
	cin >> n;
	set<int> m;
	for(int i = 0; i < n; ++i) {
		int a;
		cin >> a;
		m.insert(a);
	}
	if(m.size() < 2) {
		cout << "NO\n";
	}
	else {
		cout << *next(m.begin(), 1) << endl;
	}
	return 0;
}

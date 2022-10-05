#include <iostream>
#include <map>
 
using namespace std;
 
int main() {
  	int n;
	cin >> n;
	map<string, int> m;
	for(int i = 0; i < n; ++i) {
		string name;
		cin >> name;
		if(m[name] != 0) {
			cout << "YES\n";
		}
		else {
			cout << "NO\n";
		}
		m[name]++;
	}
 
	return 0;
}
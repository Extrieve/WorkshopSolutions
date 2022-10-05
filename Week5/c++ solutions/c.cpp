#include <iostream>
#include <set>
 
using namespace std;
 
int main() {
  	int n;
	cin >> n;
	set<string> m;
	for(int i = 0; i < n; ++i) {
		string flower, color;
		cin >> flower >> color;
		string name = flower + ' ' + color;
		m.insert(name);
	}
	cout << m.size() << endl;
	return 0;
}
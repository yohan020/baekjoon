#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int T, N, cnt;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> N;
		vector<pair<int, int>> v;
		for (int i = 0; i < N; i++) {
			int a, b;
			cin >> a >> b;
			v.push_back({ a, b });
		}
		sort(v.begin(), v.end());

		int tmp = 0;
		cnt = 1;
		for (int i = 1; i < N; i++) {
			if (v[tmp].second > v[i].second) {
				cnt++;
				tmp = i;
			}
		}
		cout << cnt << endl;
	}
	return 0;
}
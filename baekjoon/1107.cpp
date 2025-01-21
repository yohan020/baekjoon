#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

vector<bool> broken_btn;

int N, M, ans;

bool IsBroken(int n) {
	string num = to_string(n);
	for (int i = 0; i < num.size(); i++) {
		if (broken_btn[num[i] - 48]) return true;
	}
	return false;
}

int main() {
	cin >> N;
	string N_str = to_string(N);

	cin >> M;
	broken_btn.assign(10, false);
	
	for (int i = 0; i < M; i++) {
		int d;
		cin >> d;
		broken_btn[d] = true;
	}
	
	if (N == 100) {
		cout << 0;
		return 0;
	}

	ans = abs(N - 100);

	for (int i = 0; i < 1000000; i++) {
		if (!IsBroken(i)) {
			int temp = abs(N - i) + to_string(i).size();
			ans = min(ans, temp);
		}
	}
	cout << ans;
}
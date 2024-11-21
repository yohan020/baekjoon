#include <iostream>

using namespace std;

int main() {
	int DP[15];
	int t, n, k;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> k >> n;
		for (int i = 1; i < 15; i++) {
			DP[i] = i;
		}
		for (int j = 0; j < k; j++) {
			for (int x = 2; x <= n; x++) {
				DP[x] += DP[x - 1];
			}
		}
		cout << DP[n] << endl;
	}
}
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int N;
	cin >> N;
	int* n = new int[N + 1];
	for (int i = 1; i <= N; i++) {
		cin >> n[i];
	}

	int* dp = new int[N + 1];
	dp[0] = 0;
	dp[1] = n[1];
	dp[2] = n[1] + n[2];

	for (int i = 3; i <= N; i++) {
		dp[i] = max({ n[i] + n[i - 1] + dp[i - 3], n[i] + dp[i - 2], dp[i - 1] });
	}
	cout << dp[N] << endl;

	delete[] n;
	delete[] dp;

}
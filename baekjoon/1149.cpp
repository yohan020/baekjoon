#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n;
	int DP[1001][3];
	int cost[3];
	cin >> n;
	DP[0][0] = 0;
	DP[0][1] = 0;
	DP[0][2] = 0;
	for (int i = 1; i <= n; i++) {
		cin >> cost[0] >> cost[1] >> cost[2];
		DP[i][0] = min(DP[i - 1][1], DP[i - 1][2]) + cost[0];
		DP[i][1] = min(DP[i - 1][0], DP[i - 1][2]) + cost[1];
		DP[i][2] = min(DP[i - 1][0], DP[i - 1][1]) + cost[2];
	}
	cout << min(DP[n][0], min(DP[n][1], DP[n][2])) << endl;
	return 0;
}
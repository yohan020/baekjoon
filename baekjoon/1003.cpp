#include <iostream>

using namespace std;

int DP[41][2];

int main() {
	DP[0][0] = 1;
	DP[1][1] = 1;
	
	int c, x;
	cin >> c;
	for (int i = 0; i < c; i++) {
		cin >> x;
		for (int j = 2; j <= x; j++) {
			DP[j][0] = DP[j - 1][0] + DP[j - 2][0];
			DP[j][1] = DP[j - 1][1] + DP[j - 2][1];
		}
		cout << DP[x][0] << " " << DP[x][1] << endl;
	}

	return 0;
}
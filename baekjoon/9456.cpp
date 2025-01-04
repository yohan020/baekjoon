#include <iostream>
#include <vector>

using namespace std;
vector<vector<int>> sticker;
int memo[2][100001];

int max_res;
int T, n;

int main() {
	vector<vector<bool>> visited;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> n;
		sticker.assign(2, vector<int>(n, 0));

		for (int i = 0; i < 2; i++)
		{
			for (int j = 0; j < n; j++)
			{
				int test;
				cin >> test;
				sticker[i][j] = test;
			}
		}
		for (int i = 0; i < n; i++) {
			if (i == 0)
				for (int j = 0; j < 2; j++) memo[j][i] = sticker[j][i];
			else
				for (int j = 0; j < 2; j++)
					memo[j][i] = max(memo[j ^ 1][i - 1], memo[j ^ 1][i - 2]) + sticker[j][i];
		}
		cout << max(memo[0][n - 1], memo[1][n - 1]) << endl;
	}
}
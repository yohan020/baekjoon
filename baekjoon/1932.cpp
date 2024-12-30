#include <iostream>
#include <vector>
#define MAX 500

using namespace std;

vector<int> v[MAX];
vector<int> sum[MAX];

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j <= i; j++) {
			int a;
			cin >> a;
			v[i].push_back(a);
		}
	}
	sum[0].push_back(v[0][0]);
	for (int i = 1; i < n; i++) {
		for (int j = 0; j <= i; j++) {
			if (j == 0) sum[i].push_back(sum[i - 1][0] + v[i][0]);
			else if (j == i) sum[i].push_back(sum[i - 1][j - 1] + v[i][j]);
			else sum[i].push_back(max(sum[i - 1][j - 1], sum[i - 1][j]) + v[i][j]);
		}
	}
	int max = 0;
	for (int i = 0; i < n; i++) {
		if (sum[n - 1][i] > max) max = sum[n - 1][i];
	}
	cout << max;
}
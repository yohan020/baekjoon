#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
vector<vector<int>> S;

int min_res = 1000000000;

void dfs(int n, vector<int> a) {
	a.push_back(n);
	if (a.size() == N / 2) {
		int a_sum = 0;
		int b_sum = 0;
		vector<int> b;
		for (int i = 1; i <= N; i++) {
			if (find(a.begin(), a.end(), i) == a.end()) {
				b.push_back(i);
			}
		}
		for (int i = 0; i < N / 2; i++) {
			for (int j = 0; j < N / 2; j++) {
				a_sum += S[a[i] - 1][a[j] - 1];
				b_sum += S[b[i] - 1][b[j] - 1];
			}
		}
		min_res = min(min_res, abs(a_sum - b_sum));
	}
	else {
		for (int i = n + 1; i <= N; i++) {
			dfs(i, a);
		}
	}
	
}

int main() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		S.push_back(vector<int>());
		for (int j = 0; j < N; j++) {
			int temp;
			cin >> temp;
			S[i].push_back(temp);
		}
	}
	dfs(1, vector<int>());
	cout << min_res;
}
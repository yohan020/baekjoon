#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 51
using namespace std;

vector<int>tree[MAX];
vector<int>parent;
int N, target, cnt = 0;
void dfs(int node) {
	if (node == target) return;
	if (tree[node].empty() || (find(tree[node].begin(), tree[node].end(), target) != tree[node].end() && tree[node].size() == 1)) {
		cnt += 1;
		return;
	}
	for (auto n : tree[node]) {
		dfs(n);
	}
}
int main() {
	cin >> N;

	parent.assign(N, -1);
	for (int i = 0; i < N; i++) {
		cin >> parent[i];
		if (parent[i] != -1) tree[parent[i]].push_back(i);
	}

	cin >> target;

	for (int i = 0; i < N; i++) {
		if (parent[i] == -1) dfs(i);
	}
	
	cout << cnt;
}
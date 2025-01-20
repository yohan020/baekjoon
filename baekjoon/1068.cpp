#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>>tree;
vector<int> parent;
int N, target, cnt;

int main() {
	cin >> N;
	tree.resize(N);
	parent.assign(N, -1);


	for (int i = 0; i < N; i++) {
		cin >> parent[i];
		if (parent[i] != -1) tree[parent[i]].push_back(i);
	}

	cin >> target;

	delete_dfs(target);

	cnt = 0;
	for (int i = 0; i < N; i++) {
		if (i == target || tree[i].empty() && parent[i] == target) continue;
		if (isleaf(i)) {
			cnt++;
		}
	}
	int i = 0;
	for (auto t : tree) {
		cout << i++ << " | ";
		for (int i = 0; i < t.size(); i++) {
			cout << t[i] << " ";
		}
		cout << endl;
	}

	cout << cnt;

}
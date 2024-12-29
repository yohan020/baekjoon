#include <iostream>
#include <vector>

using namespace std;
#define MAX 100001

int N;
int arr[MAX];
bool visited[MAX];
vector<int> v[MAX];

void dfs(int k) {
	visited[k] = true;
	for (int i = 0; i < v[k].size(); i++) {
		int next = v[k][i];
		if (!visited[next]) {
			arr[next] = k;
			dfs(next);
		}
	}
}

int main() {
	cin >> N;
	for (int i = 0; i < N - 1; i++) {
		int a, b;
		cin >> a >> b;
		v[a].push_back(b);
		v[b].push_back(a);
	}

	dfs(1);

	for (int i = 2; i <= N; i++) {
		cout << arr[i] << '\n';
	}
}
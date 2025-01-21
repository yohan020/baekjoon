#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <cstring>
#include <queue>

#define MAX 1001

using namespace std;

int tree[MAX][MAX];
bool visited[MAX];
int N, M, res;

void bfs(int start, int dest) {
	queue<pair<int, int>> q;
	q.push({ start, 0 });
	while (!q.empty()) {
		int node = q.front().first;
		int dist = q.front().second;
		q.pop();

		visited[node] = true;

		for (int i = 1; i <= N; i++) {
			if (i == dest && tree[node][i] != 0) {
				res = dist + tree[node][i];
				return;
			}
			if (tree[node][i] != 0 && !visited[i]) {
				q.push({ i, dist + tree[node][i] });
			}
		}
	}
}

int main() {
	cin >> N >> M;
	
	for (int i = 0; i < N - 1; i++) {
		int a, b, d;
		cin >> a >> b >> d;
		tree[a][b] = d;
		tree[b][a] = d;
	}
	for (int i = 0; i < M; i++) {
		int start, dest;
		memset(visited, false, MAX);
		cin >> start >> dest;
		bfs(start, dest);
		cout << res << endl;
	}
}
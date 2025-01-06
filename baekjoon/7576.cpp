#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int M, N;
int dir[4][2] = { {-1,0},{1,0},{0,-1},{0,1} };
queue<pair<int, int>> q;

void bfs(int x, int y, vector<vector<int>>& tomato) {
	while (!q.empty()) {
		int temp_x = q.front().first;
		int temp_y = q.front().second;

		q.pop();
		for (int i = 0; i < 4; i++) {
			int ny = temp_y + dir[i][0];
			int nx = temp_x + dir[i][1];
			if (!(0 <= nx && nx < M && 0 <= ny && ny < N)) continue;
			if (tomato[ny][nx] == 0) {
				tomato[ny][nx] = tomato[temp_y][temp_x] + 1;
				q.push(make_pair(nx, ny));
			}
		}

	}
}

int main() {
	int x, y;
	cin >> M >> N;
	vector<vector<int>> tomato(N, vector<int>(M, 0));

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> tomato[i][j];
			if (tomato[i][j] == 1) {
				y = i;
				x = j;
				q.push(make_pair(x, y));
			}
		}
	}
	bfs(x, y, tomato);
	int result = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (tomato[i][j] == 0) {
				cout << -1;
				return 0;
			}
			if (result < tomato[i][j]) result = tomato[i][j];
		}
	}
	
	cout << result - 1;
}
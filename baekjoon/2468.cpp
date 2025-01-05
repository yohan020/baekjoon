#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int rel = 0;
int N;
int dir[4][2] = { {0, -1}, {0, 1}, {-1, 0}, {1, 0} };
vector<vector<bool>> visited;

void dfs(int x, int y) {
	visited[x][y] = true;
	for (int i = 0; i < 4; i++) {
		int nx = x + dir[i][0];
		int ny = y + dir[i][1];
		if (0 <= nx && nx < N && 0 <= ny && ny < N) {
			if (!visited[nx][ny]) dfs(nx, ny);
		}
	}
}

int main() {
	int max_area = 0;
	cin >> N;
	vector<vector<int>> area(N, vector<int>(N, -1));
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> area[i][j];
			if (area[i][j] > max_area) max_area = area[i][j];
		}
	}
	for (int w = 0; w <= max_area; w++) {
		int safe_area = 0;
		visited.assign(N, vector<bool>(N, false));
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (area[i][j] < w) visited[i][j] = true;
			}
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (!visited[i][j]) {
					safe_area++;
					dfs(i, j);
				}
			}
		}
		rel = max(rel, safe_area);
		
		
	}
	cout << rel;
}
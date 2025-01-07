#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
using namespace std;

int M, N, H;
int dir[6][3] = { {-1,0,0},{1,0,0},{0,-1,0},{0,1,0}, {0,0,1}, {0,0,-1} };
queue<tuple<int, int, int>> q;

void bfs(vector<vector<vector<int>>>& tomato) {
	while (!q.empty()) {
		int temp_x = get<0>(q.front());
		int temp_y = get<1>(q.front());
		int temp_z = get<2>(q.front());

		q.pop();
		for (int i = 0; i < 6; i++) {
			int ny = temp_y + dir[i][0];
			int nx = temp_x + dir[i][1];
			int nz = temp_z + dir[i][2];

			if (!(0 <= nx && nx < M && 0 <= ny && ny < N && 0 <= nz && nz < H)) continue;
			if (tomato[nz][ny][nx] == 0) {
				tomato[nz][ny][nx] = tomato[temp_z][temp_y][temp_x] + 1;
				q.push({ nx, ny, nz });
			}
		}

	}
}

int main() {
	cin >> M >> N >> H;
	vector<vector<vector<int>>> tomato(H, vector<vector<int>>(N, vector<int>(M, 0)));

	for (int i = 0; i < H; i++) {
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < M; k++) {
				cin >> tomato[i][j][k];
				if (tomato[i][j][k] == 1) {
					q.push({k, j, i});
				}
			}
		}
	}
	bfs(tomato);
	int result = 0;


	for (int i = 0; i < H; i++) {
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < M; k++) {
				if (tomato[i][j][k] == 0) {
					cout << -1;
					return 0;
				}
				if (result < tomato[i][j][k]) result = tomato[i][j][k];
			}
			
		}
	}
	cout << result - 1 << endl;
	
}
#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> field;
int N, M, cnt;
int r, c, d;
int dir[4][2] = { {-1,0}, {0, 1}, {1, 0}, {0, -1} };

bool AllClean(int x, int y) {
	for (int i = 0; i < 4; i++) {
		int ny = y + dir[i][0];
		int nx = x + dir[i][1];
		if (field[ny][x] == 1) continue;
		if (field[ny][nx] == 0) return false;
	}
	return true;
}

bool forward(int x, int y, int d) {
	int ny = y + dir[d][0];
	int nx = x + dir[d][1];
	if (field[ny][nx] == 1 || field[ny][nx] == 2) return false;
	return true;
}

void move(int x, int y, int d) {
	while(true) {
		if (field[y][x] == 0) {
			field[y][x] = 2;
			cnt++;
		}
		if (!AllClean(x, y)) {
			do {
				d--;
				if (d < 0) d += 4;
			} while (!forward(x, y, d));
			int ny = y + dir[d][0];
			int nx = x + dir[d][1];
			x = nx;
			y = ny;
		}
		else {
			int ny = y - dir[d][0];
			int nx = x - dir[d][1];
			if (field[ny][nx] == 1) return;
			else {
				x = nx;
				y = ny;
			}
		}
	}
}

int main() {
	cin >> N >> M;
	cin >> r >> c >> d;
	field.assign(N, vector<int>(M, 0));
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> field[i][j];
		}
	}
	cnt = 0;
	move(c, r, d);
	cout << cnt;
}
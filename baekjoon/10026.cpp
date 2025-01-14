#include <iostream>
#include <vector>

using namespace std;

int N;
int dir[4][2] = { {0,1},{1,0},{0, -1},{-1, 0} };

vector<vector<int>> visited;

bool isAllvisited() {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (visited[i][j] == 0) return false;
		}
	}
	return true;
}

void dfs(int x, int y, vector<vector<char>>board, int& count) {
	visited[y][x] = count;
	for (int i = 0; i < 4; i++) {
		int ny = y + dir[i][0];
		int nx = x + dir[i][1];
		if (!(0 <= nx && nx < N && 0 <= ny && ny < N)) continue;
		if (board[y][x] == board[ny][nx] && visited[ny][nx] == 0) dfs(nx, ny, board, count);
	}
}

int main() {
	
	cin >> N;
	vector<vector<char>> board(N, vector<char>(N, '#'));
	vector<vector<char>> board2(N, vector<char>(N, '#'));
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> board[i][j];
			if (board[i][j] == 'G') board2[i][j] = 'R';
			else board2[i][j] = board[i][j];
		}
	}

	visited.assign(N, vector<int>(N, 0));
	int count = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (visited[i][j] == 0) dfs(j, i, board, ++count);
		}
	}
	cout << count << " ";

	visited.assign(N, vector<int>(N, 0));
	count = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (visited[i][j] == 0) dfs(j, i, board2, ++count);
		}
	}

	cout << count << endl;
	
}
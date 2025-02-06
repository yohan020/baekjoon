#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> board;
vector<vector<int>> dp;
int dir[4][2] = {{-1,0}, {0, 1}, {1, 0}, {0, -1}}; 
int M, N;

int DFS(int x, int y) {
    if (x == N - 1 && y == M - 1) return 1;
    if (dp[y][x] != -1) return dp[y][x];

    dp[y][x] = 0;

    for (int i = 0; i < 4; i++) {
        int nx = x + dir[i][1];
        int ny = y + dir[i][0];

        if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
        if (board[y][x] > board[ny][nx]) {
            dp[y][x] += DFS(nx, ny);
        }
    }
    return dp[y][x];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> M >> N;
    board.assign(M, vector<int>(N));
    dp.assign(M, vector<int>(N, -1));
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            cin >> board[i][j];
        }
    }
    

    cout << DFS(0, 0);
}

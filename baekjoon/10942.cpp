#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

vector<int>n_list;
bool dp[2001][2001];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M, a, b;
    cin >> N;
    n_list.resize(N+1);
    memset(dp, false, sizeof(dp));

    for (int i = 1; i <= N; i++) cin >> n_list[i];

    for (int i = 1; i < N; i++) {
        dp[i][i] = true;
        if (n_list[i] == n_list[i+1]) {
            dp[i][i+1] = true;
        } else {
            dp[i][i+1] = false;
        }
    }
    dp[N][N] = true;

    for (int i = N - 2; i > 0; i--) {
        for (int j = i + 2; j <= N; j++) {
            dp[i][j] = (n_list[i] == n_list[j]) && dp[i+1][j-1];
        }
    }

    cin >> M;
    for (int i = 0; i < M; i++) {
        cin >> a >> b;
        if (dp[a][b]) {
            cout << "1\n";
        } else {
            cout << "0\n";
        }
    }
}

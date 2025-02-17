#include <iostream>

using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int DP[201][201] = {0, };
    int N, K;
    cin >> N >> K;

    DP[0][0] = 1;
    for (int i = 1; i <= K; i++) {
        DP[i][0] = 1;
        for (int j = 1; j <= N; j++) {
            DP[i][j] = DP[i-1][j] + DP[i][j-1];
        }
    }
    cout << DP[K][N];
}
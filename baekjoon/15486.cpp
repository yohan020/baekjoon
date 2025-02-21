#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N;
    int result = 0;
    int max_idx = -1;
    cin >> N;

    vector<pair<int, int>> consult(N);
    vector<int> dp(N+1, 0);

    for (int i = 0; i < N; i++) {
        int a, b;
        cin >> a >> b;
        consult[i] = make_pair(a, b);
    }

    for (int i = N-1; i >= 0; i--) {
        if (i+consult[i].first <= N) {
            dp[i] = max(consult[i].second + dp[i+consult[i].first], dp[i+1]);
        } else {
            dp[i] = dp[i+1];
        }
    }
    cout << dp[0];
}
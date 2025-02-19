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
    vector<int> dp(N, 0);

    for (int i = 0; i < N; i++) {
        int a, b;
        cin >> a >> b;
        consult[i] = make_pair(a, b);
    }

    for (int i = N-1; i >= 0; i--) {
        if ((i+1) + consult[i].first > N + 1) {
            dp[i] = 0;
        } else {
            
            //for (int j = N-1; j >= i+consult[i].first; j--) { // 이거 시간초과 임
            //    if (max_pay < dp[j]) {
            //        max_pay = dp[j];
            //    }
            //}
            if (i+consult[i].first <= max_idx) {
                dp[i] = consult[i].second + max(dp[max_idx], dp[i+consult[i].first]);
            } else {
                dp[i] = consult[i].second + dp[i+consult[i].first];
            }
            result = max(result, dp[i]);
            if (result == dp[i]) max_idx = i;
        }
    }
    cout << result;
}
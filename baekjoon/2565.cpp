#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    int result = 1;
    int dp[101]; // dp[i]는 line[i].second를 마지막으로 하는 가장 긴 증가하는 수
    vector<pair<int, int>> line;

    cin >> N;
    for (int i = 0; i < N; i++) {
        int a, b;
        cin >> a >> b;
        line.push_back(make_pair(a, b));
    }
    sort(line.begin(), line.end());

    for (int i = 0; i < N; i++) dp[i] = 1;

    for (int i = 1; i < N; i++) {
        for (int j = 0; j < i; j++) {
            if (line[i].second > line[j].second) { // i가 커지면서 탐색 범위가 한개 증가한 숫자가 다른 숫자보다 높은지 확인
            // 높은 경우 dp값을 더해주면서 증가해 나가기, i보다 왼쪽에 있는 수와 전부 비교하다 보니 가장 큰 값을 고르기 위해서는 기존의 dp[i]와 비교하는 것도 중요
                dp[i] = max(dp[j] + 1, dp[i]);
                result = max(dp[i], result);
            }
        }
    }
    cout << N-result; // 가장 긴 큰 수를 N에 다 빼주면 제거해야하는 전선 길이를 알 수 있다.
}
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int DP[100000] = {0, };
    int n;

    cin >> n;
    
    vector<int>arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    DP[0] = arr[0];
    int result = arr[0];

    for (int i = 1; i < n; i++) {
        DP[i] = max(DP[i - 1] + arr[i], arr[i]);
        result = max(DP[i], result);
    }
    cout << result;
}
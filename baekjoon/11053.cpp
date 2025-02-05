#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int DP[1000];

    int N;
    cin >> N;

    vector<int>arr(N);

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
        DP[i] = 1;
    }
    
    int result = 1;
    for (int i = 1; i < N; i++) {
        for (int j = 0; j < i; j++) {
            if (arr[j] < arr[i]) DP[i] = max(DP[j] + 1, DP[i]);
            result = max(result, DP[i]);
        }
    }
    cout << result;
}

#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int DP[1001] = {0, };

    int N;
    cin >> N;

    vector<int>arr(N);

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }
    DP[0] = 0;
    DP[1] = 1;
    for (int i = 1; i < N; i++) {
        if (arr[i] < arr[i-1]) {
            if (i > 1) {
                if (arr[i] > arr[i - 2]) {
                    DP[i + 1] = DP[i - 1] + 1; 
                } else {
                    DP[i + 1] = DP[i];
                }
            } else {
                DP[i + 1] = DP[i];
            }
        }
        else {
            DP[i + 1] = DP[i] + 1;
        }
    }
    for (int i = 0; i <= N; i++) {
        cout << DP[i] << " ";
    }
    cout << endl;
    cout << DP[N];
}

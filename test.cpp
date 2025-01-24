#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<long> decreasing_n;

void dfs(long start) {
    decreasing_n.push_back(start);
    int n = start % 10;
    for (int i = n - 1; i >= 0; i--) {
        long num = start * 10 + i;
        dfs(num);
    }
}

int main() {
    int N;
    cin >> N;

    for (int i = 9; i >= 0; i--) {
        dfs(i);
    }
    sort(decreasing_n.begin(), decreasing_n.end());
    if (N >= decreasing_n.size()) {
        cout << -1;
        return 0;
    }
    cout << decreasing_n[N];
    return 0;
}
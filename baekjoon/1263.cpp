#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

vector<pair<int, int>> todo;
int N;

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        int a, b;
        cin >> a >> b;
        todo.push_back({a, b});
    }
    sort(todo.begin(), todo.end(), [](const pair<int,int> &a, const pair<int,int> &b) {
        return a.second < b.second;
    });
    
    int res = todo[N-1].second;
    for (int i = N - 1; i >= 1; i--) {
        res -= todo[i].first;
        if (todo[i-1].second < res) {
            res = todo[i-1].second;
        }
    }
    res -= todo[0].first;
    if (res < 0) res = -1;
    cout << res;
}
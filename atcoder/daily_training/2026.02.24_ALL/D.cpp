#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N;
    cin >> N;
    int *time = new int[N];
    vector<pair<int, int>> time_map;

    for(int i = 0; i < N; i++) {
        cin >> time[i];
    }
    for(int i = 0; i < N; i++) {
        time_map.push_back(make_pair(time[i], i));
    }
    sort(time_map.begin(), time_map.end());

    for(int i = 0; i < 3; i++) {
        cout << time_map[i].second + 1 << " ";
    }
}
#include <iostream>
#include <vector>
#include <utility>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N;
    cin >> N;

    priority_queue<pair<int, int>,vector<pair<int, int>>, greater<pair<int, int>>> schedule;
    priority_queue <int, vector<int>, greater<int>> classroom;
    for (int i = 0; i < N; i++) {
        int start, end;
        cin >> start >> end;
        schedule.push({start, end});
    }

    classroom.push(schedule.top().second);
    schedule.pop();
    while (!schedule.empty()) {
        if (classroom.top() <= schedule.top().first) {   
            classroom.pop();
            classroom.push(schedule.top().second);
        } else {
            classroom.push(schedule.top().second);
        }
        schedule.pop();
    }

    cout << classroom.size();
}
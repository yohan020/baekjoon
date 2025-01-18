#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
#define INF 98765432
#define MAX 1001
using namespace std;

int N, M;
int start, des;
vector<pair<int, int>> bus[MAX];
int dist[MAX];
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;

void dijkstra(int start) {
	q.push({ 0, start });
	dist[start] = 0;
	while (!q.empty()) {
		int cost = q.top().first;
		int now_city = q.top().second;
		q.pop();
		if (dist[now_city] < cost) continue;

		for (int i = 0; i < bus[now_city].size(); i++) {
			int temp_cost = cost + bus[now_city][i].second;
			int next_city = bus[now_city][i].first;
			if (temp_cost < dist[next_city]) {
				dist[next_city] = temp_cost;
				q.push({ temp_cost, next_city });
			}
		}
	}
}

int main() {
	int a, b, c;
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> N >> M;
	bus[0].push_back({ 0,0 });
	memset(dist, INF, sizeof(dist));
	for (int i = 0; i < M; i++) {
		cin >> a >> b >> c;
		bus[a].push_back({ b, c });
	}
	cin >> start >> des;
	dijkstra(start);
	cout << dist[des];
}
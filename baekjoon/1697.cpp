#include <iostream>
#include <queue>

using namespace std;

int visited[100001][2];

int bfs(int N, int K) {
  queue<int> q;
  q.push(N);
  visited[N][0] = 1;
  while (!q.empty()) {
    int now = q.front();
    q.pop();
    if (now == K) {
      return visited[now][1];
    }
    if (now * 2 < 100001 && visited[now*2][0] == 0) {
      visited[now*2][1] = visited[now][1] + 1;
      visited[now*2][0] = 1;
      q.push(now * 2);
    }
    if (0<now && visited[now-1][0] == 0 ) {
      visited[now-1][1] = visited[now][1] + 1;
      visited[now-1][0] = 1;
      q.push(now - 1);
    }
    if (now<100000 && visited[now+1][0] == 0 ) {
      visited[now+1][1] = visited[now][1] + 1;
      visited[now+1][0] = 1;
      q.push(now + 1);
    }
  }
}

int main() {
  for (int i = 0; i < 100001; i++) {
    visited[i][0] = 0;
    visited[i][1] = 0;
  }
  int N, K;
  cin >> N >> K;
  cout << bfs(N, K);
}
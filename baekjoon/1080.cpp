#include <iostream>
#include <vector>

using namespace std;

// 행렬은 같은 곳 두번 뒤집으면 의미 없음!

void reverse(vector<string> &A, int x, int y) {
  for (int i = x; i < x + 3; i++) {
    for (int j = y; j < y + 3; j++) {
      if (A[i][j] == '0') A[i][j] = '1';
      else A[i][j] = '0';
    }
  }
}
int N, M, count;

int main() {
  count = 0;
  string temp;
  cin >> N >> M;
  vector<string> A;
  vector<string> B;
  for (int i = 0; i < N; i++) {
    cin >> temp;
    A.push_back(temp);
  }
  for (int i = 0; i < N; i++) {
    cin >> temp;
    B.push_back(temp);
  }

  for (int i = 0; i < N-2; i++) {
    for (int j = 0; j < M-2; j++) {
      if (A[i][j] != B[i][j]) {
        reverse(A, i, j);
        count++;
      }
    }
  }

  bool flag = true;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      if (A[i][j] != B[i][j]) {
        flag = false;
      }
    }
  }
  if (flag) {
    cout << count << endl;
  }
  else {
    cout << -1 << endl;
  }
}
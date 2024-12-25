#include <iostream>
#include <vector>

using namespace std;

void reverse(vector<string> &A, int x, int y) {
  for (int i = x; i < x + 3; i++) {
    for (int j = y; j < y + 3; j++) {
      A[i][j] = (A[i][j] == '0') ? '1' : '0';
    }
  }
}

int main() {
  int N, M, count = 0;
  cin >> N >> M;
  vector<string> A(N), B(N);

  for (int i = 0; i < N; i++) {
    cin >> A[i];
  }
  for (int i = 0; i < N; i++) {
    cin >> B[i];
  }

  for (int i = 0; i < N - 2; i++) {
    for (int j = 0; j < M - 2; j++) {
      if (A[i][j] != B[i][j]) {
        reverse(A, i, j);
        count++;
      }
    }
  }

  bool flag = true;
  for (int i = 0; i < N && flag; i++) {
    for (int j = 0; j < M && flag; j++) {
      if (A[i][j] != B[i][j]) {
        flag = false;
      }
    }
  }

  cout << (flag ? count : -1) << endl;
}
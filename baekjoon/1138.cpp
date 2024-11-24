#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n, idx;
  cin >> n;
  vector<int> v(n), line(n);
  for (int i = 0; i < n; i++) {
    cin >> v[i];
  }
  for (int i = 1; i <= n; i++) {
    idx = 0;
    for (int j = 0; j  < v[i-1]; j++) {
      if (line[idx] != 0) {
        j--;
      }
      idx++;
    }
    while (line[idx] != 0) idx++;
    line[idx] = i;
  }
  for (int i = 0; i < n; i++) {
    cout << line[i] << " ";
  }
  return 0;
}
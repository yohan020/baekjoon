#include <iostream>
#include <algorithm>
using namespace std;

int DP[12];

int main() {
	
	int n, T;
	cin >> n;
	DP[1] = 1; // 이것들은 초기 값
	DP[2] = 2;
	DP[3] = 4;
	for (int i = 4; i < 12; i++) DP[i] = DP[i - 1] + DP[i - 2] + DP[i - 3]; // 1, 2, 3을 이용하여 덧셈 식을 만들어줌
	// 피보나치 수열로 이루어져 있었음
	for (int i = 0; i < n; i++) {
		cin >> T;
		cout << DP[T] << endl;
	}
	
}

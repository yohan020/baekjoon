//2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
//아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.

#include <iostream>

using namespace std;

int DP[100001];

int main() {
	int n;
	cin >> n;

	DP[1] = 1;
	DP[2] = 2;

	for (int i = 3; i <= n; i++) {
		DP[i] = (DP[i - 1] + DP[i - 2]) % 10007;
	}
	cout << DP[n];
}
//정수 X를 3으로 나누거나 2로 나누거나 1을 빼서 1로 만드는 문제


#include <iostream>
#include <algorithm>
using namespace std;

int DP[1000000];

int main() {
	
	int n;
	cin >> n;
	
	for (int i = 2; i <= n; i++) {
		DP[i] = DP[i - 1] + 1; // i는 1 뺴면 i - 1이 되므로 우선 한번 더해줌
		if (i % 2 == 0) {
			DP[i] = min(DP[i], DP[i / 2] + 1); // 2로 나눈 경우가 더 작은 지 확인해줌
		}
		if (i % 3 == 0) {
			DP[i] = min(DP[i], DP[i / 3] + 1); // 3으로 나눈 경우가 더 작은 지 확인해줌
		}
	}
	cout << DP[n];
}

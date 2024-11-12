//���� X�� 3���� �����ų� 2�� �����ų� 1�� ���� 1�� ����� ����


#include <iostream>
#include <algorithm>
using namespace std;

int DP[1000000];

int main() {
	
	int n;
	cin >> n;
	
	for (int i = 2; i <= n; i++) {
		DP[i] = DP[i - 1] + 1; // i�� 1 ���� i - 1�� �ǹǷ� �켱 �ѹ� ������
		if (i % 2 == 0) {
			DP[i] = min(DP[i], DP[i / 2] + 1); // 2�� ���� ��찡 �� ���� �� Ȯ������
		}
		if (i % 3 == 0) {
			DP[i] = min(DP[i], DP[i / 3] + 1); // 3���� ���� ��찡 �� ���� �� Ȯ������
		}
	}
	cout << DP[n];
}

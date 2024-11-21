#include <iostream>
#include <algorithm>
using namespace std;

int DP[12];

int main() {
	
	int n, T;
	cin >> n;
	DP[1] = 1; // �̰͵��� �ʱ� ��
	DP[2] = 2;
	DP[3] = 4;
	for (int i = 4; i < 12; i++) DP[i] = DP[i - 1] + DP[i - 2] + DP[i - 3]; // 1, 2, 3�� �̿��Ͽ� ���� ���� �������
	// �Ǻ���ġ ������ �̷���� �־���
	for (int i = 0; i < n; i++) {
		cin >> T;
		cout << DP[T] << endl;
	}
	
}

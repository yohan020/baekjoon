//2��n ũ���� ���簢���� 1��2, 2��1 Ÿ�Ϸ� ä��� ����� ���� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
//�Ʒ� �׸��� 2��5 ũ���� ���簢���� ä�� �� ���� ����� ���̴�.

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
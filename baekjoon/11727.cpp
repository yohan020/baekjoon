// 2��n ���簢���� 1��2, 2��1�� 2��2 Ÿ�Ϸ� ä��� ����� ���� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
//�Ʒ� �׸��� 2��17 ���簢���� ä�� �Ѱ��� ���̴�.

#include <iostream>
using namespace std;

int main() {
	int DP[1001];
	int n;
	cin >> n;
	DP[1] = 1;
	DP[2] = 3;

	for (int i = 3; i <= n; i++) {
		DP[i] = (DP[i - 1] + 2 * DP[i - 2]) % 10007;
	}
	cout << DP[n];
}
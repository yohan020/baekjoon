#include <iostream>
#include <algorithm>
using namespace std;

int DP[301]; // DP[i]�� i��° ��ܱ��� �������� ���� �ִ� ����
int score[301];

int main() {
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> score[i];
    }

    // �ʱⰪ ����
    DP[1] = score[1];
    if (n >= 2) {
        DP[2] = score[1] + score[2];
    }

    // DP ��ȭ�� ����
    for (int i = 3; i <= n; i++) {
        DP[i] = max(DP[i - 2] + score[i], DP[i - 3] + score[i - 1] + score[i]); // ù��°�� ��ĭ ���ö������
        // �ι� °�� ��ĭ ��ĭ �ö���� ��
    }

    cout << DP[n] << endl;

    return 0;
}
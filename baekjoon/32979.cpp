#include <iostream>
#include <vector>
using namespace std;

int main() {
	int N, T, temp;
	cin >> N;
	cin >> T;
	vector<int> hand(N * 2);
	vector<int> apart_floor(T);
	for (int i = 0; i < N * 2; i++) {
		cin >> hand[i];
	}
	for (int i = 0; i < T; i++) {
		int temp;
		cin >> temp;
		apart_floor[i] = temp - 1; // i�� 1���ʹ� 1�� �� ������ ����
	}
	int floor = 0;
	for (int i = 0; i < T; i++) {
		floor += apart_floor[i];
		floor %= (N * 2);
		cout << hand[floor] << " ";
	}
}
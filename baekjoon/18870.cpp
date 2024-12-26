#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX = 1000001;
int arr[MAX];

int main() {
	int n;
	cin >> n;

	vector<int> v;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];

		v.push_back(arr[i]);
	}

	sort(v.begin(), v.end());

	v.erase(unique(v.begin(), v.end()), v.end()); // unique�� �ߺ��� ���ҵ��� �� �ڷ� �����ִ� ������ �Ѵ�. �׷��鼭 �ߺ��� ���۵Ǵ� ��ġ�� ��ȯ�ϸ鼭 �ű⼭���� end���� �ߺ��� ������
	//unique�� �ð� ���⵵�� O(N)�̰� erase���� O(N)�̹Ƿ� �ش� ��ɾ�� O(N)�̴�.


	for (int i = 0; i < n; i++) {
		int idx = lower_bound(v.begin(), v.end(), arr[i]) - v.begin();
		// lower_bound�� ã���� �ϴ� ���� ó������ ��Ÿ���� ��ġ�� ��ȯ��
		// lower_bound�� ���� Ž�� (�߰� ������ �������� ã�� ���� �߰������� ũ�� ������, ������ �������� �̵��ϸ鼭 ã�´�.) �̹Ƿ� �ð� ���⵵�� O(logN)�̴�.
		cout << idx << " ";
	}
}
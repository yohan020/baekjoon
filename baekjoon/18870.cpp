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

	v.erase(unique(v.begin(), v.end()), v.end()); // unique는 중복된 원소들을 맨 뒤로 보내주는 역알을 한다. 그러면서 중복이 시작되는 위치를 반환하면서 거기서부터 end까지 중복을 제거함
	//unique의 시간 복잡도는 O(N)이고 erase또한 O(N)이므로 해당 명령어는 O(N)이다.


	for (int i = 0; i < n; i++) {
		int idx = lower_bound(v.begin(), v.end(), arr[i]) - v.begin();
		// lower_bound는 찾고자 하는 값이 처음으로 나타나는 위치를 반환함
		// lower_bound는 이진 탐색 (중간 지점을 기준으로 찾는 값이 중간값보다 크면 오른쪽, 작으면 왼쪽으로 이동하면서 찾는다.) 이므로 시간 복잡도는 O(logN)이다.
		cout << idx << " ";
	}
}
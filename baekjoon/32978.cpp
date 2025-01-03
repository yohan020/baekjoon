#include <iostream>
#include <vector>

using namespace std;

int main() {
	int N;
	cin >> N;
	vector<string> ingridient(N);
	vector<string> real(N-1);
	for (int i = 0; i < N; i++) {
		cin >> ingridient[i];
	}
	for (int i = 0; i < N - 1; i++) {
		cin >> real[i];
	}
	for (int i = 0; i < N - 1; i++) {
		for (int j = 0; j < ingridient.size(); j++) {
			if (ingridient[j] == real[i]) {
				ingridient.erase(ingridient.begin() + j);
				break;
			}
		}
	}
	cout << ingridient[0] << endl;
}
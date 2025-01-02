#include <iostream>
#include <vector>

using namespace std;

vector<int> operand;

int N;
int min_result = 1000000001;
int max_result = -1000000001;

void dfs(vector<int>operator_cnt, vector<char> operator_list) {
	vector<int> temp_operator_cnt = operator_cnt;
	for (int i = 0; i < 4; i++) {
		if (temp_operator_cnt[i] > 0) {
			temp_operator_cnt[i]--;
			switch (i) {
			case 0:
				operator_list.push_back('+');
				break;
			case 1:
				operator_list.push_back('-');
				break;
			case 2:
				operator_list.push_back('*');
				break;
			case 3:
				operator_list.push_back('/');
				break;
			}
			if (operator_list.size() == N - 1) {
				int result = operand[0];
				for (int i = 0; i < N - 1; i++) {
					switch (operator_list[i]) {
					case '+':
						result += operand[i + 1];
						break;
					case '-':
						result -= operand[i + 1];
						break;
					case '*':
						result *= operand[i + 1];
						break;
					case '/':
						result /= operand[i + 1];
						break;
					}
				}
				min_result = min(min_result, result);
				max_result = max(max_result, result);
				return;
			}
			dfs(temp_operator_cnt, operator_list);
			operator_list.pop_back();
			temp_operator_cnt[i]++;
		}

	}
}

int main() {
	vector<int> operator_cnt(4);
	vector<char> operator_list;

	cin >> N;

	for (int i = 0; i < N; i++) {
		int temp;
		cin >> temp;
		operand.push_back(temp);
	}

	for (int i = 0; i < 4; i++) {
		int temp;
		cin >> temp;
		operator_cnt[i] = temp;
	}
	dfs(operator_cnt, operator_list);
	cout << max_result << endl;
	cout << min_result << endl;
}
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
int L, C;
vector<char>str;
string temp;

bool isValid() {
	int moum = 0, zaum = 0;
	for (char c : temp) {
		if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
			moum++;
		}
		else {
			zaum++;
		}
	}
	return moum >= 1 && zaum >= 2;
}

void encode(int i) {
	temp += str[i];
	if (temp.length() == L) {
		if (isValid()) {
			cout << temp << endl;
		}
		return;
	}
	for (int j = i + 1; j < C; j++) {
		encode(j);
		temp.pop_back();
	}
}

int main() {
	cin >> L >> C;
	str.assign(C, ' ');
	for (int i = 0; i < C; i++) {
		cin >> str[i];
	}
	sort(str.begin(), str.end());
	for (int i = 0; i <= C - L; i++) {
		temp = "";
		encode(i);
	}
	
}
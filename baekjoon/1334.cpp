#include <iostream>
#include <string>

using namespace std;

int len; // 숫자 길이
string n_str; // 펠린드롬화 하기 위한 문자열

void palindrome() {
	for (int i = 0; i < len / 2; i++) {
		n_str[len - (1 + i)] = n_str[i];
	}
	cout << n_str;
}

bool compareStrings(const string& str1, const string& str2) {
	for (int i = 0; i < str1.size(); i++) {
		if (str1[i] > str2[i]) return true; // str1이 더 큼
		if (str1[i] < str2[i]) return false; // str2가 더 큼
	}
}

void check() {
	string a = ""; // 앞 자리수를 역으로 나열한 수
	string b = ""; // 뒤 자리수를 추출한 수
	for (int i = 0; i < len / 2; i++) {
		a += n_str[len / 2 - (1 + i)];
		if (len % 2 == 0) {
			b += n_str[len / 2 + i];
		}
		else {
			b += n_str[len / 2 + i + 1];
		}
	}
	if (a == b) { // 1더한 값이 펠린드롬일 경우
		cout << n_str;
		return;
	}

	if (compareStrings(a, b)) { // a > b
		palindrome();
	}
	else {
		int mid_idx;
		if (len % 2 == 0) { // 중간 지점 인덱스
			mid_idx = len / 2 - 1; 
		}
		else {
			mid_idx = len / 2;
		}
		while (n_str[mid_idx] == '9') {
			n_str[mid_idx] = '0';
			mid_idx--;
		}
		n_str[mid_idx] += 1; // 중간 지점에 1 더함
		palindrome();
	}
}

int main() {
	cin >> n_str;
	int idx = n_str.length();
	
	while (idx >= 1) { // 1을 더할 때 반올림 될 경우
		if (n_str[idx - 1] != '9') break;
		n_str[idx - 1] = '0';
		idx--;
	}
	if (idx == 0) { // 999...9 인 경우
		len = n_str.length();
		n_str = '1';
		for (int i = 0; i < len; i++) {
			n_str += '0';
		}
		len++;
	}
	else {
		n_str[idx - 1] += 1; // X99...9( X != 9) 인 경우
	}
	
	len = n_str.length();
	check();
}
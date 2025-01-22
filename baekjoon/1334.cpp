#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int len; // ���� ����
string n_str; // �縰���ȭ �ϱ� ���� ���ڿ�

void palindrome() {
	for (int i = 0; i < len / 2; i++) {
		n_str[len - (1 + i)] = n_str[i];
	}
	cout << n_str;
}

bool compareStrings(const string& str1, const string& str2) {
	for (int i = 0; i < str1.size(); i++) {
		if (str1[i] > str2[i]) return true; // str1�� �� ŭ
		if (str1[i] < str2[i]) return false; // str2�� �� ŭ
	}
}

void check() {
	string a = ""; // �� �ڸ����� ������ ������ ��
	string b = ""; // �� �ڸ����� ������ ��
	for (int i = 0; i < len / 2; i++) {
		a += n_str[len / 2 - (1 + i)];
		b += n_str[len / 2 + i];
		//a += pow(10, i) * (n_str[i] - '0');
		//b += pow(10, i) * (n_str[len - (i+1)] - '0');
		
	}
	// cout << a << endl << b << endl;
	if (a == b) { // 1���� ���� �縰����� ���
		cout << n_str << endl;
		return;
	}

	if (compareStrings(a, b)) { // a > b
		palindrome();
	}
	else {
		int mid_idx;
		if (len % 2 == 0) { // �߰� ���� �ε���
			mid_idx = len / 2 - 1; 
		}
		else {
			mid_idx = len / 2;
		}
		while (n_str[mid_idx] == '9') {
			n_str[mid_idx] = '0';
			mid_idx--;
		}
		n_str[mid_idx] += 1; // �߰� ������ 1 ����
		palindrome();
	}
}

int main() {
	cin >> n_str;
	int idx = n_str.length();
	
	while (idx >= 1) {
		if (n_str[idx - 1] != '9') break;
		n_str[idx - 1] = '0';
		idx--;
	}
	if (idx == 0) {
		len = n_str.length();
		n_str = '1';
		for (int i = 0; i < len; i++) {
			n_str += '0';
		}
		len++;
	}
	else {
		n_str[idx - 1] += 1; // 199���� ���ڸ� ó���ϱ� ����
	}
	
	len = n_str.length();
	check();
}
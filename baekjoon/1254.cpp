#include <iostream>
using namespace std;

// 이 문제는 부분적인 팰린드롬을 찾으면 되는 거 였음
// 만약 부분적인 팰린드롬이 없다면 그냥 맨 끝 글자를 기준으로 팰린드롬을 만들어주면되는 거고

bool isPalindrome(const string &s) {
  int left = 0;
  int right = s.size() - 1;
  while(left < right) {
    if(s[left] != s[right]) {
      return false;
    }
    left++;
    right--;
  }
  return true;
}

int main() {
  string S;
  cin >> S;

  int n = S.size();
  for(int i = 0; i < n; ++i) {
    if(isPalindrome(S.substr(i))) { // substr(i) 는 i번째 문자부터 시작하는 부분 문자열
      // 그래서 그 부분 문자열이 팰린드롬이면 i만큼(팰린드롬이 아닌부분) 만큼 앞에 더 해주면 팰린드롬이 된다
      cout << i + n << endl;
      return 0;
    }
  }

  cout << 2 * n - 1 << endl;
  return 0;
}
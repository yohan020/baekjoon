#include <iostream>
#include <algorithm>
using namespace std;

int DP[301]; // DP[i]는 i번째 계단까지 도달했을 때의 최대 점수
int score[301];

int main() {
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> score[i];
    }

    // 초기값 설정
    DP[1] = score[1];
    if (n >= 2) {
        DP[2] = score[1] + score[2];
    }

    // DP 점화식 적용
    for (int i = 3; i <= n; i++) {
        DP[i] = max(DP[i - 2] + score[i], DP[i - 3] + score[i - 1] + score[i]); // 첫번째는 두칸 씩올라왔을때
        // 두번 째는 두칸 한칸 올라왔을 때
    }

    cout << DP[n] << endl;

    return 0;
}
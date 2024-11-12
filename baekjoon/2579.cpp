//계단 오르기 게임은 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임이다.
//1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
//2. 연속된 세 개의 계단을 모두 밟아서는 안 된다.단, 시작점은 계단에 포함되지 않는다.
//3. 마지막 도착 계단은 반드시 밟아야 한다.

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
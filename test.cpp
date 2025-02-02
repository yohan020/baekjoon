#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string code;
    int DP[5001] = {0,};

    cin >> code;
    DP[0] = 1;
    DP[1] = 1;
    if (code[0] == '0') {
        cout << 0;
        return 0;
    }
    for (int i = 1; i < code.length(); i++) {
        string n = code.substr(i - 1,2);
        int temp = stoi(n);
        if (code[i] == '0') {
            if (temp == 10 || temp == 20) {
                DP[i + 1] = DP[i - 1];
            } else {
                cout << 0;
                return 0;
            }
        }
        else if (code[i-1] == '0' || 26 < temp) {
            DP[i + 1] = DP[i];
        }
        else if (9 < temp && temp < 27) {
            if (i == code.length() - 2 && code[i + 1] == '0') {
                DP[i + 1] = DP[i];
            } else {
                DP[i + 1] = DP[i] + DP[i - 1];
            }
            
        }
    }
    cout << DP[code.length()] % 1000000 << endl;
}

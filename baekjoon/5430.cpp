#include <iostream>
#include <deque>
#include <string>
using namespace std;

void DELETE(deque<int> &arr, int D_idx) {
    if (D_idx == 0) arr.pop_front();
    else arr.pop_back();
}

void string_to_deque(string n_arr, deque<int> &arr) {
    if (n_arr == "[]") {
        return;
    }
    int temp1 = 0;
    for (int i = 1; i < n_arr.length() - 1; i++) {
        if (n_arr[i] == ',') {
            arr.push_back(temp1);
            temp1 = 0;
        } else {
            temp1 = temp1 * 10 + (n_arr[i] - '0');
        }
    }
    arr.push_back(temp1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int t, arr_len;
    string func;
    

    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> func;
        cin >> arr_len; // 입력받을 숫자의 수
        deque<int> arr;


        string num_arr;
        int n_idx = 1;
        cin >> num_arr;

        string_to_deque(num_arr, arr);

        int R_count = 0;
        int D_idx = 0; // 0이 앞자리 1이 뒷자리
        bool can_print = true;

        for (int j = 0; j < func.length(); j++) {
            if (func[j] == 'R') {
                R_count++;
            } 
            else if(func[j] == 'D') {
                if (arr.size() == 0) {
                    cout <<"error\n";
                    can_print = false;
                    break;
                } else {
                    DELETE(arr, R_count % 2);
                }
                
            }
        }
        if (can_print) {
            cout << "[";
            if (arr_len == 0 || arr.size() == 0) { // 입력된 숫자가 없거나 큐가 비어있을 때
                cout << "]\n";
            }
            else if (R_count % 2 == 0) {
                for (int j = 0; j < arr.size() - 1; j++) {
                    cout << arr[j] << ",";
                }
                cout << arr[arr.size() - 1] << "]\n";
            } else {
                for (int j = arr.size() - 1; j >= 1; j--) {
                    cout << arr[j] << ",";
                }
                cout << arr[0] <<"]\n";
            }
        }
    }
}
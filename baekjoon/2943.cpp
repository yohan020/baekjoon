#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    vector<int>TOP(N);
    for (int i = 0; i < N; i++) cin >> TOP[i];
    stack<int>st;
    vector<int>Result(N);
    for (int i = N - 1; i >= 0; i--) {
        if (st.size() == 0) st.push(i);
        else {
            while(!st.empty()) {
                if (TOP[i] > TOP[st.top()]) {
                    Result[st.top()] = i + 1;
                    st.pop();
                } else {
                    break;
                }
            }
            st.push(i);
        }
    }
    for (int i = 0; i < N; i++) cout << Result[i] << " ";
}
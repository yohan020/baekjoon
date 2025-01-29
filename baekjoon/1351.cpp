#include <iostream>
#include <unordered_map>

using namespace std;
long N;
int P, Q;

unordered_map<long, long> A;

long An(long n) {
    if (A.find(n) != A.end()) return A[n];
    return A[n] = An(n / P) + An(n / Q);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
 
    A[0] = 1;
    cin >> N >> P >> Q;
    cout << An(N);

}
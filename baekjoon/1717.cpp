#include <iostream>

using namespace std;

int SET[1000001];

int find_parent(int a) {
    if (SET[a] == a) return a;
    else return SET[a] = find_parent(SET[a]); // 부모노드 업데이트
}

void Union(int a, int b) {
    int a_root = find_parent(a);
    int b_root = find_parent(b);
    if (a_root == b_root) return;
    SET[a_root] = b_root;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, comm, a, b;
    cin >> n >> m;

    for (int i = 0; i <= n; i++) SET[i] = i;

    for (int i = 0; i < m; i++) {
        cin >> comm >> a >> b;
        if (comm) {
            if (find_parent(a) == find_parent(b)) {
                cout << "YES\n";
            } else {
                cout << "NO\n";
            }
        } else {
            Union(a, b);
        }
    }
}
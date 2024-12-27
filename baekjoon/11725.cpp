#include <iostream>
#include <cmath>
using namespace std;
int N, max_node;
int* tree;
void add_edge(int n1, int n2) {
	for (int i = 0; i < max_node; i++) {
		if (tree[i] == n1) {
			if (tree[i * 2 + 1] == 0) {
				tree[i * 2 + 1] = n2;
				break;
			}
			else if (tree[i * 2 + 2] == 0) {
				tree[i * 2 + 2] = n2;
				break;
			}
		}
		else if (tree[i] == n2) {
			if (tree[i * 2 + 1] == 0) {
				tree[i * 2 + 1] = n1;
				break;
			}
			else if (tree[i * 2 + 2] == 0) {
				tree[i * 2 + 2] = n1;
				break;
			}
		}
	}
}

int find_parent(int n) {
	for (int i = 0; i < max_node; i++) {
		if (tree[i] == n) {
			return tree[(i - 1) / 2];
		}
	}
}

int main() {
	cin >> N;

	max_node = pow(2, N) - 1;
	tree = new int[max_node];
	for (int i = 0; i < max_node; i++) {
		tree[i] = 0;
	}
	tree[0] = 1;
	int n1, n2;
	for (int i = 0; i < N - 1; i++) {
		cin >> n1 >> n2;
		add_edge(n1, n2);
	}
	for (int i = 2; i <= N; i++) {
		cout << find_parent(i) << endl;
	}
}
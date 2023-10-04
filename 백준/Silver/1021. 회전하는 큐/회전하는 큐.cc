#include <iostream>
#include <deque>

using namespace std;

int main() {


    deque<int> dq; 
    int idx; // 삭제할 원소가 있는 인덱스 
    int count = 0; // 답

    int n, m, x;
    cin >> n >> m;

    for (int i = 1; i <= n; i++)
        dq.push_back(i);

    while (m--) {
        cin >> x;

        for (int i = 0; i < dq.size(); i++) {
            if (dq[i] == x) {
                idx = i;
                break;
            }
        }

        // 앞에서부터
        if (idx <= dq.size() / 2) {
            while (1) {
                if (dq.front() == x) {
                    dq.pop_front();
                    break;
                }
                ++count;
                dq.push_back(dq.front());
                dq.pop_front();
            }
        }
        else { // 뒤에서부터
            while (1) {
                if (dq.front() == x) {
                    dq.pop_front();
                    break;
                }
                ++count;
                dq.push_front(dq.back());
                dq.pop_back();
            }
        }
    }

    cout << count;

    return 0;
}
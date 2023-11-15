#include <iostream>
#include <stack>
using namespace std;

/*
NO가 나오는 경우
1. 스택에 '('가 없는데 ')'가 입렫된 경우
2. 모든 괄호를 소비했는데 스택에 괄호가 남아있는 경우'('
3. 
*/




int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;
	string ps;
	stack<char> st;

	cin >> T;
	for (int i = 0; i < T; i++) {

		stack<char> st;
		cin >> ps;
		bool isNo = true;
		

		//입력한 괄호를 조건에따라 스택에 조작
		for (int i = 0; i < ps.size(); i++) {
			if (ps[i] == '(') {  // '('가 나오면 일단 push
				st.push('(');
			}
			else {  // ')'일때
				if (st.empty()) {    // ')'가 나왔는데 스택이 비었다? >> '('이 없다(짝이 안맞는다) >> NO
					cout << "NO" << endl;
					isNo = false;
					break;
				}
				st.pop();
			}
		}

		if (isNo) {
			// 입력한 모든 괄호를 사용한 경우
			if (st.empty()) {
				cout << "YES" << endl;
			}
			//입력한걸 모두 사용했는데 스택에 무언가 남아있다? >> '('가 남아있다(오괄호는 push하지 않았기 때문)  >> 짝이 안맞는다 >> NOw
			else {
				cout << "NO" << endl;
			}
		}
	}

	return 0;
	
}
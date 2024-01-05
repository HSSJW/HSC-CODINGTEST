#include <iostream>
#include <stack>
using namespace std;



int main() {

	string exp;

	cin >> exp; //중위 표기식 입력받기

	stack<char> sign;

	for (int i = 0; i < exp.length(); i++) {

		// 문자면 출력
		if (exp[i] >= 'A' && exp[i] <= 'Z') {
			cout << exp[i];
		}

		else if (exp[i] == ')') { //닫는 괄호이면 여는 괄호 나올때까지 부호 출력

			while (sign.top() != '(') { //여는 괄호가 아닌 동안 반복
				cout << sign.top();
				sign.pop();
			}
			sign.pop(); // 여는 괄호 제거
		}

		else if (!sign.empty() && (((sign.top() == '/') || (sign.top() == '*')) && ((exp[i] == '-') || (exp[i] == '+')))) {
			
			while (!sign.empty() && sign.top() != '(') { //부호 다 털기
				cout << sign.top();
				sign.pop();
			}
			
			sign.push(exp[i]);
		}

		else if (!sign.empty() && (((sign.top() == '+') || (sign.top() == '-')) && ((exp[i] == '-') || (exp[i] == '+')))) { //우선순위가 같은 부호
			
			//하나 출력후 psuh
			cout << sign.top();
			sign.pop();
			sign.push(exp[i]);
		}

		else if (!sign.empty() && (((sign.top() == '*') || (sign.top() == '/')) && ((exp[i] == '*') || (exp[i] == '/')))) { //우선순위가 같은 부호
			cout << sign.top();
			sign.pop();
			sign.push(exp[i]);
		}

		else
			sign.push(exp[i]);

	}





	while (!sign.empty()) {  //남은 부호 다 털기
		if (sign.top() != '(') {
			cout << sign.top();
			sign.pop();
		}
		else
			sign.pop();
	}


	return 0;

}
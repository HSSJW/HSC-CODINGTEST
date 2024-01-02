#include <iostream>
#include <stack>
#include <algorithm>
using namespace std;



int main() {

	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	string input, target;
	stack<char> st;

	cin >> input >> target;

	for (int i = 0; i < input.length(); i++) {
		st.push(input[i]);
		
		//타겟의 마지막 글자와 일치하는 부분 찾기
		if (input[i] == target[target.length() - 1] && st.size() >= target.length()) { //찾았다

			string tmp;

			for (int j = 0; j < target.length(); j++) { //일치하는 부분 삭제
				
				tmp.push_back(st.top());  //뒤부터 target길이만큼을 tmp로 복사
				st.pop();
		}
			
			reverse(tmp.begin(), tmp.end()); //st에서 뽑은 문자열 뒤집기

			if(tmp != target){ //일치하지않으면 다시 st에 push
				
				for (int j = 0; j < tmp.length(); j++) {
					st.push(tmp[j]);

				}
			}

			
		}
	}
	string result;

	if (st.empty())//비었으면
		cout << "FRULA";
	else {
		int len = st.size(); //스택에 저장된 문자개수 저장

		for (int i = 0; i < len; i++) { //스택에 저장된 문자열 뒤집기위해 string변수에 저장
			result.push_back(st.top());
			st.pop();
		}

		reverse(result.begin(), result.end()); //뒤집기
		cout << result;
	}



	return 0;

}
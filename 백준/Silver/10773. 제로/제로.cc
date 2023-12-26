#include <iostream>
#include <vector>
using namespace std;





int main() {

	int n;
	int sum = 0;
	int input = NULL;
	vector<int> stack;  //순서대로 저장  0이 아닌 수 >> push 0 >> pop

	cin >> n;


	for (int i = 0; i < n; i++) {

		cin >> input;
		if (input != 0) //스택에 저장
			stack.push_back(input);
		else //0 입력하면 삭제
			stack.pop_back();
	
	}

	while (!stack.empty()) { //스택이 비어있지 않는 동안에
		sum += stack.back();
		stack.pop_back();
		
	}

	cout << sum;
	return 0;

}
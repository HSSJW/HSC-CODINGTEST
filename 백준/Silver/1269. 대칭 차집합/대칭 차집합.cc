#include <iostream>
#include <map>
using namespace std;

map<int, bool> m;


int main() {

	int a, b; //각각의 원소의 개수
	int input;

	cin >> a >> b;


	for (int i = 0; i < a; i++) { //집합 a의 원소들 초기화
		cin >> input;

		m[input] = true;
	}



	for (int i = 0; i < b; i++) {
		cin >> input;

		if (m[input] == true)
			m.erase(input); // key가 input인 데이터 제거
		else
			m[input] = true;
	}

	cout << m.size();

	return 0;

}
#include <iostream>
#include <map>
using namespace std;




int main() {
	int n;
	map<string, int> name;
	string maxBook;
	int max = 0;

	cin >> n;

	string input;

	for (int i = 0; i < n; i++) {
		cin >> input;


		if (name.find(input) == name.end()) { //처음 입력된 경우
			name.insert({ input, 1 });
		}
		else { //이미 입력받았었던 책인 경우
			name.find(input)->second++; //해당 key값의 value값 ++
		}
	}
	 
	auto iter = name.end();
	iter--;

	//map은 자동으로 오름차순으로 정리되며 저장된다
	for (iter; iter != name.begin(); iter--) { //자동으로 name의 맨앞 key부터 check에 초기화

		if (iter->second >= max) {
			max = iter->second;
			maxBook = iter->first;
		}
	}

	if (iter->second >= max) {
		max = iter->second;
		maxBook = iter->first;
	}

	cout << maxBook;

	return 0;
}
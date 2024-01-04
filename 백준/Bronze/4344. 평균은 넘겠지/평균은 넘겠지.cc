#include <iostream>
using namespace std;

int main() {

	int n;
	int student;

	cin >> n;

	for (int i = 0; i < n; i++) {
		int score[1000];
		double count = 0; //평균을 넘는 학생 수
		double avg = 0, sum = 0;
		cin >> student;

		for (int j = 0; j < student; j++) {
			cin >> score[j];
			sum += score[j];
		}


		avg = sum / student;

		for (int j = 0; j < student; j++) {
			if (score[j] > avg)
				count++;
		}

		cout << fixed;
		cout.precision(3); //소수점 자리 설정
		cout << count / student * 100 << "%" << "\n";

	}

	return 0;
}
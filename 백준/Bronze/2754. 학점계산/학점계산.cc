#include <iostream>
#include <string>
using namespace std;

double getGradePoint(const string& grade) {
    if (grade == "A+") return 4.3;
    else if (grade == "A0") return 4.0;
    else if (grade == "A-") return 3.7;
    else if (grade == "B+") return 3.3;
    else if (grade == "B0") return 3.0;
    else if (grade == "B-") return 2.7;
    else if (grade == "C+") return 2.3;
    else if (grade == "C0") return 2.0;
    else if (grade == "C-") return 1.7;
    else if (grade == "D+") return 1.3;
    else if (grade == "D0") return 1.0;
    else if (grade == "D-") return 0.7;
    else return 0.0;
}

int main() {
    string grade;
    cin >> grade;

    double gradePoint = getGradePoint(grade);
    cout << fixed;
    cout.precision(1);
    cout << gradePoint << endl;

    return 0;
}

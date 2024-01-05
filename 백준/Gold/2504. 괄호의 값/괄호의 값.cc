#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main() {
    string input;
    cin >> input;

    stack<char> s;
    int result = 0;
    int temp = 1; // 현재 괄호에 곱해질 값

    for (int i = 0; i < input.length(); ++i) {
        char current = input[i];

        if (current == '(') {
            s.push('(');
            temp *= 2;
        } else if (current == '[') {
            s.push('[');
            temp *= 3;
        } else if (current == ')') {
            if (s.empty() || s.top() != '(') {
                cout << "0\n";
                return 0;
            }

            if (input[i - 1] == '(') {
                result += temp;
            }

            s.pop();
            temp /= 2;
        } else if (current == ']') {
            if (s.empty() || s.top() != '[') {
                cout << "0\n";
                return 0;
            }

            if (input[i - 1] == '[') {
                result += temp;
            }

            s.pop();
            temp /= 3;
        }
    }

    if (!s.empty()) {
        cout << "0\n";
    } else {
        cout << result << "\n";
    }

    return 0;
}

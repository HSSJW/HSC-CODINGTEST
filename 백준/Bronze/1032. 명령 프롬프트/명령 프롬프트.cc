#include <iostream>
using namespace std;

int main()
{

	int n;

	cin >> n;

	string* file = new string[n];
	string result;

	for (int i = 0; i < n; i++)
	{
		cin >> file[i];
	}
	result = file[0];

	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			for (int k = 0; k < result.size(); k++)
			{
				//fc(file[i], file[j], result);

				if (file[i][k] != file[j][k])
					result.replace(k, 1, "?");
			}

	cout << result;

	return 0;
}
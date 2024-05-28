#include <iostream>
using namespace std;



int main()
{

	int n, l;
	int Array[1001] = {0};
	int drop_point;
	int count = 0;
	int max = 0;

	cin >> n >> l;

	for (int i = 0; i < n; i++)
	{
		cin >> drop_point;
		Array[drop_point] = 1;    //물새는 위치를 1로 표시
		
		if (max < drop_point)
			max = drop_point;
	}

	for (int i = 1; i <= max; i++)
	{
		if (Array[i] == 1)
		{
			count++;
			i += (l - 1);
		}

	}

	cout << count;

	return 0;
}
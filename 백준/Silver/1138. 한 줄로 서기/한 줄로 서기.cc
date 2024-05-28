#include <iostream>
using namespace std;

/*
지시대로 선다
사람들은 왼쪽 자신보다 큰사람이 몇명인지 기억
키는 모두 다름


사람수 1<=n<=10
어떻게 서야하는지 출력
*/




int main()
{

	int n;
	cin >> n;   //사람 수 n 입력받는다

	int* Array = new int[n + 1];
	int* fake = new int[n+1];
	int* list = new int[n];
	int count = 0;
	


	for (int i = 0; i < n; i++)
	{
		cin >> Array[i + 1];
		list[i] = 0;
	}
	int how = 0;
	for (int j = n; j > 0; j--)
	{
		count = 0;
		
		while (true)
		{
			if (Array[j] == 0)
			{
				for (int k = 0; k < n; k++)
					fake[k] = list[k];
				
				for (int k = count; k < how; k++)
				{
					fake[k+1] = list[k];
				}
				fake[count] = j;
				
				for (int k = 0; k < n; k++)
					list[k] = fake[k];
				break;
			}
			
			Array[j]--;
			count++;
		}
		how++;
	}

	for (int i = 0; i < n; i++)
	{
		cout << list[i] << " ";
	} 




	return 0;
}
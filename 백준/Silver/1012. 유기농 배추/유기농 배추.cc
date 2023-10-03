#include <iostream>
using namespace std;


//상하좌우에서 배추를 찾아서 0으로 바꾸는 함수
void find_one(int** array, int m, int n, int row, int col)
{
	array[row][col] = 0; // 현재위치(배추가있는 위치)를 0으로 초기화하고

	if (row > 0 && array[row - 1][col] == 1)
		find_one(array, m, n, row - 1, col);

	
		if (row < m - 1 && array[row + 1][col] == 1)
		find_one(array, m, n, row + 1, col);
	if (col > 0 && array[row][col - 1] == 1)
		find_one(array, m, n, row, col - 1);
	if (col < n - 1 && array[row][col + 1] == 1)
		find_one(array, m, n, row, col + 1);

}

int main()
{
	int t, m, n, k;
	int row, col; //배추좌표를 입력받을 변수
	

	cin >> t;

	for (int p = 0; p < t; p++)
	{
		cin >> m >> n >> k;
		int count = 0;

		//이중포인터는 포인터를 가르키는 포인터
		int** array = new int* [m];

		for (int i = 0; i < m; i++)
		{
			array[i] = new int[n];
		}


		for (int i = 0; i < k; i++)
		{
			cin >> row >> col;

			array[row][col] = 1;
		}

		for (int i = 0; i < m; i++)
			for (int j = 0; j < n; j++)
			{
				if (array[i][j] == 1)
				{
					count++;
					find_one(array, m, n, i, j);
				}
			}


		cout << count << endl;

		for (int i = 0; i < m; i++)
			delete[] array[i];

	}

	return 0;
}
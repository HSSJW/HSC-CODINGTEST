#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int count, height[1000] = {0};

	int up[500] = { 0 };
	int a[1000]={0}, b[1000] = {0}, max = 0, num_a = 0, num_b = 0;

	scanf("%d", &count);
	

	for (int k = 0; k < count; k++)
	{
		scanf("%d", &height[k]);

	}



	for (int i = 0; i < count; i++)
	{
	gogo:
		if (i == count - 1)
			break;

		
		if (height[i] < height[i + 1])
		{	
			a[num_a] = height[i];
			num_a++;

			
			for(int p = i; p < count; p++)
				if (p == count - 1)
				{
					b[num_b] = height[p];
					i = p + 1;
					break;
				}

				else if (height[p] >= height[p + 1])
				{	
						b[num_b] = height[p];
						num_b++;
						i = p + 1;
						goto gogo;
				}
		}


	}

	for (int t = 0; t <= num_a; t++)
		if (max < b[t] - a[t])
			max = b[t] - a[t];

	printf("%d", max);

	return 0;
}
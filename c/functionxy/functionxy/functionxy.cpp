#include<iostream>
using namespace std;
int main()
{
	// domain (x)  1,2,3,4,5    codomain(y) 2*x = 2,4,6,8,10
	int y{ 0 };
	for (int x = 1; x <= 9; x=x+2)
	{
		y = 2 * x;
	}

	return 0;
}
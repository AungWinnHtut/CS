#include<iostream>
#include<array>

using namespace std;

template <typename T>
T max1(T a, T b, T c)
{
	T max = a;
	if (b > max)
	{
		max = b;
	}
	if (c > max)
	{
		max = c;
	}
	return max;
}
int main()
{
	int a = 2;
	int b = 4;
	int c = 22;
	int iArr[10] = { 0 };
	array<int, 5> oArr{0,2,4,6,8};
	cout << "modified array vales" << endl;
	for (int& k : oArr)
	{
		k = 2 * k;
		cout << k << " ";
	}
	cout << endl;
	cout << "original array" << endl;
	for (int k : oArr)
	{
			cout << k << " ";
	}
	
}



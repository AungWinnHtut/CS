#include<iostream>
#include<vector>

using namespace std;
int  main(void)
{
	int a;
	vector<int> marks(4);
	marks[1] = 12;
	marks.at(3)= 22; 
	cout <<marks.at(2);

	//cout << a;
	
	return 0;
}
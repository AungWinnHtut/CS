#include<vector>
#include<iostream>
using namespace std;

int main()
{


	vector<int>  data(5); //auto zero
	data.at(0) = 1;
	data.at(1) = 2;
	data.at(2) = 3;
	data.at(3) = 4;
	data.at(4) = 5;
	data.push_back(6);
	data.pop_back();
	vector<int>::iterator it;
	it = data.begin()+2;
	data.insert(it, 6, 100);

	for (int item : data)
	{
		cout << item<<endl;
	}
}
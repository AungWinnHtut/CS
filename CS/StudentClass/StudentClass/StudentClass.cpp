#include<iostream>
using namespace std;
class Student {
private:
	int64_t pocket_money{0};
	string name{ "anonymous" };
public: 
	Student() {
		//name = "anonymous";
	}
	explicit Student(int64_t amount, string nickname) : pocket_money{ amount }, name{ nickname } {}
	int64_t landMoney()
	{
		int64_t landMoney = pocket_money;		
		return landMoney;
	}
	void borrowMoney(Student Right)
	{
		pocket_money += Right.landMoney();
	}
	void showMoney()
	{
		cout <<name<<" has "<< pocket_money <<" $"<< endl;
	}
	void minusMoney()
	{
		pocket_money =0;
	}
};


int sum(int x, int y) //pass by value
{
	return x + y;
}

void swap(int* x, int* y) //pass by reference
{
	int temp = 0;
	temp = *x;
	*x = *y;
	*y = temp;
}

int main()
{
	int a = 3;
	int b = 4;
	int c = sum(a, b);
	swap(a, b);
	cout << "a= " << a << endl;
	cout << "b= " << b << endl;


	return 0;
}

int main1()
{
	if (4)
	{
		cout << "True" << endl;
	}
	

	return 0;
}

#include<iostream>
using namespace std;

class Account {
private:
	string name;
public:
	explicit Account(string accountName) {
		name = accountName;
	}
	void setName(string accountName)
	{
		name = accountName;
	}
	string getName()
	{
		return name;
	}
};


/*
Length
----------
-feet:float
-inches:float
-----------
+Length(feet:float,inches:float)
+setFeet(feet:float)
+getFeet():float
+setInches(feet:float)
+getInches():float
+totalInches(): float
+totalFeet():float
*/

class Length {
private:
	float feet;
	float inches;
public:
	//Length(){} //default constructor
	explicit Length(float ifeet, float iInches) : feet{ ifeet },inches{iInches}//
	{
		
	}
	void setFeet(float inputFeet)
	{
		feet = inputFeet;
	}
	float getFeet() const
	{
		return feet;
	}
	void setInches(float inputInches)
	{
		inches = inputInches;
	}
	float getInches() const
	{
		return inches;
	}
	float totalInches()
	{
		return (feet * 12) + inches;
	}
	float totalFeet()
	{
		return (inches / 12) + feet;
	}

};


/*
BankAccount
----------------
-balance:int
-name:string
----------------
constructor BankAccount(initialBalance:int,userName:string)
+setBalance(newBalance:int)
+getBalance():int
+setName(newName:string)
+getName():string
+deposit(newAmount:int)

*/
class BankAccount {
private: 
	int balance;
	string name;
	
public:
	BankAccount(int initialBalance, string userName) :balance{ initialBalance }, name{ userName } {
		if (initialBalance > 0)
		{
			balance = initialBalance;
		}
		
	}
	void setBalance(int newBalance) {
		balance = newBalance;
	}
	int getBalance() const {
		return balance;
	}

	void setName(string userName) {
		name = userName;
	}
	string getName() const {
		return name;
	}
	void deposit(int newAmount)
	{
		balance += newAmount;
	}
};

int main()
{
	
	BankAccount AgAg{ 10000, "Aung Aung" };
	BankAccount MgMg{ 20000, "Maung Maung" };
	AgAg.deposit(30000);
	MgMg.deposit(50000);
	cout << AgAg.getBalance() << endl;
	cout << MgMg.getBalance() << endl;

	return 0;
}
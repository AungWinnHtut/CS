#include<iostream>
#include<conio.h>
using namespace std;

//define all operationCode / Instruction SET
//std IO 1
#define READ 10
#define WRITE 11

//Accumulator 2
#define LOAD 20
#define STORE 21

//Arithmetic operation 3
#define ADD 30
#define SUBTRACT 31
#define DIVIDE 32
#define MULTIPLY 33

//Transfer of Control  (JUMP) 4
#define BRANCH 40
#define BRANCHNEG 41
#define BRANCHZERO 42
#define HALT 43

int accumulator = 0;
int instructionCounter = 0;
int memory[100]{ 0 };                 //0-49 instructions      50-99 data
int instructionRegister = 0;
int operationCode = 0;
int operand = 0;

void read();
void write();
void load();
void store();
void add();
void sub();
void div();
void mul();
void branch();
void branchneg();
void branchzero();
void halt();

int main()
{
	memory[0] = 1050;
	memory[1] = 1051;
	memory[2] = 2050;
	memory[3] = 3151;
	memory[4] = 2153;
	memory[5] = 1153;
	memory[6] = 4300;

	while (memory[instructionCounter] != 0)
	{
		instructionRegister = memory[instructionCounter];
		operationCode = instructionRegister / 100;
		operand = instructionRegister % 100;

		switch (operationCode)
		{
		case READ: read(); break;
		case WRITE: write(); break;
		case LOAD: load();  break;
		case STORE: store();  break;
		case ADD: add();  break;
		case SUBTRACT: sub();  break;
		case DIVIDE: div();  break;
		case MULTIPLY: mul();  break;
		case BRANCH: branch();  break;
		case BRANCHNEG: branchneg();  break;
		case BRANCHZERO: branchzero();  break;
		case HALT: halt(); break;
		}
		instructionCounter++;
	}
	return 0;
}


void read()
{
	cout << "Please Enter Data: ";
	cin >> memory[operand];
}
void write()
{
	cout << "The result is : " << memory[operand];
}

void load()
{
	accumulator = memory[operand];
}

void store()
{
	memory[operand] = accumulator;
}

void add()
{
	accumulator += memory[operand];
}
void sub()
{
	accumulator -= memory[operand];
}
void div()
{
	accumulator /= memory[operand];
}
void mul()
{
	accumulator *= memory[operand];
}

void branch()
{
	instructionCounter = operand;
}

void branchneg()
{
	if (accumulator < 0)
	{
		instructionCounter = operand;
	}	
}

void branchzero()
{
	if (accumulator ==  0)
	{
		instructionCounter = operand;
	}
}

void halt()
{
	_getch();
	exit(0);
}
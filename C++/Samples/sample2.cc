//DEFINITION AND USE OF VARIABLES

#include <iostream>
using namespace std;

int gVar1;             //global variable
int gVar2 = 2;         //explicit initialization

int main()
{
    char ch('A');        //local variable initialized
                        //or ch char = 'A';
    
    cout << "Value of gVar1: " << gVar1 << endl;
    cout << "Value of gVar2: " << gVar2 << endl;
    cout << "Character in ch " << ch << endl;

    int sum, number = 3;     //local variable with ir
                             //without initialization.
    
    sum = number + 5;

    cout << "Value of sum: " << sum << endl;

    return 0;
}


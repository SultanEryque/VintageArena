/*******************************************************
A program with some functions and comments
******************************************************/

#include <iostream>
using namespace std;

void line(), message();     // Prototype

int main()
{
    cout << "Hello! The program starts in main()."
         << endl;
    line();
    message();
    line();
    cout << "At the end of main()." << endl;

    return 0;
}

void line()              //To draw line.
{
    cout << "_______________________" << endl;
}
void message()           //To display a message.
{
    cout << "In function message()." << endl;
}

#include <iostream>
using namespace std;

int main()
{
    cout << "\nSize of Fundamental Types\n" << endl;
    cout << " Type               Number of Bytes\n"
         << "______________________________________" <<  endl;
    cout << "Char:               " << sizeof(char) << endl;
    cout << "short:              " << sizeof(short) << endl;
    cout << "int:                " << sizeof(int) << endl;
    cout << "long:               " << sizeof(long) << endl;
    cout << "float:              " << sizeof(float) << endl;
    cout << "double:             " << sizeof(double) << endl;
    cout << "double long:        " << sizeof(long double) << endl;

    return 0;
} 

#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

int main()
{
    double x = 0.123456,
           y = 23.987,
           z = -123.456;

    string title = 
    "\nA simple formatting output program\n";

    cout << left << title << endl;
    cout << left << setw(15) << setfill('0') << x << endl;
    cout << right << setw(12) 
         << setprecision(2) << fixed 
         << y << endl;
    cout << setw(10) << setprecision(4) 
         << scientific << endl;

    return 0;
}

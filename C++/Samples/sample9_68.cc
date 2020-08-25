// Enters a character and outputs it
// octal, decimal and hexadecimal code.

#include <iostream>         // Declaration of cin, cout
#include <iomanip>          // For manipulators bieng called with arguements
#include <string>           // For string manipulation
using namespace std;

int main()
{
    int number = ' ';
    cout << "The white space code is as follows: "
         << number << endl;

    char ch;
    string prompt = 
           "\nPlease Enter a character followed by"
                                       "<Return>: ";
    cout << prompt;
    cin >> ch;                 // Read a character
    number = ch;
    
    cout << "The character " << ch 
         << "has code " << number << endl;

    cout << uppercase          // For hex-digits
         << "       octal  decimal  hexadecimal\n"
         << oct << setw(8) << number
         << dec << setw(8) << number 
         << hex << setw(8) << number << endl;
    return 0;
}

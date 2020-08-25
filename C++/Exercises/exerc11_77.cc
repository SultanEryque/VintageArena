// The following program displays an integer in octal, 
// decimal and hexadecimal.

#include <iostream>
#include <string>
using namespace std;

int main()
{
    int num;
    string s = 
    "_____WELCOME TO THE INT CONVERTER______";

    cout << s << endl;;
    cout << "Please input an integer and press <Return>" << endl;
    cin >> num;

    char ch = num;
    cout << "Here is your output..." << endl;
    cout << "Character: "  << ch 
         << "\nOctal: " << oct << num
         << "\nDecimal: " << dec << num
         << "\nHexadecimal: " << hex << num << endl;
   
    cout << "Bye";

    return 0;
}

#include <iostream>
#include <climits>       //DEFINiTION OF INT_MIN
using namespace std;

int main()
{
    cout << "Range of type int and unsigned in"
         <<endl << endl;
    cout << "Types     Minimum     Maximum"
         << endl
         << "_____________________________"
         << endl;
    cout << "int        " << INT_MIN << "    "
                          << INT_MAX << endl;
    cout <<"unsigned int" << "    0      "
                          << UINT_MAX << endl;

return 0;
}

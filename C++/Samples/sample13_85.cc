#include <iostream>
using namespace std;

int main()
{
    int i(2), j(8);
    
    cout << i++ << endl;        //output: 2
    cout << i   << endl;        //output: 3
    cout << j-- << endl;        //output: 8
    cout << --j << endl;        //output: 6

    return 0;
}

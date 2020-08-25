//calculating power with the standard function pow()

#include <iostream>      //Delcaration of cout
#include <cmath>         //For importing math modules like pow()
using namespace std;

int main()
{
    double x = 2.5, y;

    //compiler automatically pick correct syntax or throws errors.

    //computes x to power 3
    y = pow(x, 3.0);              //ok
    y = pow(x, 3);                //ok, compiler automatically converts 3 to a float

    cout << "x raised to power 3 is equal to " << y << endl;

    //calculation with pow is also possible
    cout << "2 + (5.0 raised to the power of 2.5) is "
         << 2.0 + pow(5.0, x) << endl;
}

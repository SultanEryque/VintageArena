// Program to find square roots of numbers

#include <iostream>          
#include <cmath>
#include <cstdlib>
using namespace std;

int fst = 4;
float nd = 12.57;
double rd = 0.0121;

int main()
{
    int x, kq;
    double y;
    double z;
    x = sqrt( fst);
    y = sqrt( nd);
    z = sqrt( rd);    
    unsigned int den;  
    cout << "Welcome to finding squareroots" << endl;
    cout << "For Example... " << endl;
    cout << "Number" << "     " << " Square Root" << endl
         << fst << "            " << x << endl
         << nd << "        " << y << endl
         << rd << "        " << z << endl;
    cout << "Your Turn: " << endl
         << "Input Integer: " << endl;
    cin >> den;
    
    kq = sqrt( den);

    cout << "square root of " << den << " " << "is" << " "<< kq << endl;

   return 0;
}

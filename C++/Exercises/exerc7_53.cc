#include <iostream>      //for cout streaming
#include <cstdlib>       //declairing tge randoms eg srand, rand
#include <string>        // for string manipulation
using namespace std;

int main()
{
    string message ("\nLearn fron your mistakes!");
    cout << message << endl;

    int len = message.length();
    cout << "Length of the string: " << len << endl;

    // And a random number in addition
    int a = 12.5, b;
    unsigned int seed;
    seed = a;
    srand( seed);

    b = rand();
    cout << "\nRandom number: " << b << endl;
    return 0;
}

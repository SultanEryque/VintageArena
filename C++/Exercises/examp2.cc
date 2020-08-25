#include <iostream>
using namespace std;

void what(), yes();      //prototype

int main()
{
    what();              
    cout << "a happy day!." << endl;
    yes();             
    cout << "what a happy day!" <<  endl;

    return 0;
}
void what()              //defines the function
{ 
   cout << "Oh what" << endl;
}
void yes()               //defines the function
{
    cout << "Oh yes" << endl;
}

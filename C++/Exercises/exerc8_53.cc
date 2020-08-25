#include <iostream>
#include <string>
using namespace std;


int main()
{
    string name("\nI have learned something new again! "),
           prompt ("Enter 2 line of txt: "),
           name1,
           name2,
           name3;
                   
    int len = name.length();
    cout << name << ", is " << len << "\ncharacters long inclusive of whutespace."
          << endl;

   cout << prompt;
   getline( cin, name1);
   getline( cin, name2);
  
   name3 = name1 + " * " + name2;

   cout << "Final string is " << name3 << endl;

   return 0;
}
     
    


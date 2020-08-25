// an article program

#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

int main()
{
    string name = "Article Number",
           number = "Number of Pieces",
           price = "Price per Piece",
           title = "Article Shop",
           prompt = "kindly enter the following";

    int  num, num1;
    double num3;

    cout << title << endl;
    cout << prompt; 
    cout << "       " << endl;
    cout <<  name  << endl;
    
    cin >> num;
   
    cout << number << endl;
    
    cin >> num1;

    cout << price << endl;
    
    cin >> num3;

    cout << "\nHere are your details" << endl;
    cout << "\n\tArticle Number    Number of Pieces    Price per Piece";
    cout << "\n\t" 
         << setw(8)   << num
         << setw(16)  << num1 
         << right << fixed << setprecision(2)
         << setw(16) << num3 << " Dollar" << endl;
     
   cout << "Bye" << endl;
 
   return 0;
}

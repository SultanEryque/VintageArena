// Inputs an article lable and a price

#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

int main()
{
    string label;
    double price;

    cout << "\nPlease enter an article label: ";

    // Input the label(15 characters maximu)
    cin.width(16);        // or cin = setw(6)
    cin >> label;
   
    cin.sync();             // clears and resets the buffer
    cin.clear();            // any error flag that may be set

    cout << "\nEnter the price of the article: ";
    cin >> price;

    // Controlling output
    cout << fixed << setprecision(2)
         << " \nArticle: "
         << " \n  Label: " << label 
         << " \n  Price: " << price << endl;

     // .. The Program to be continued

     return 0;
}


// Read two floating points' values of double precision A and B, corresponding to two student's grades. After this, calculate the student's average, considering that grade A has weight 3.5 and B has weight 7.5. Each grade can be from zero to ten, always with one digit after the decimal point. Don’t forget to print the end of line after the result, otherwise you will receive “Presentation Error”. Don’t forget the space before and after the equal sign.

#include<bits/stdc++.h>
using namespace std;

int main() {
    double A, B, avarage;

    cin>>A;
    cin>>B;

    avarage = ((A*3.5)+(B*7.5))/11.0;

    cout << fixed << setprecision(5);
    cout << "MEDIA = " << avarage << "\n"; 

    return 0;
}


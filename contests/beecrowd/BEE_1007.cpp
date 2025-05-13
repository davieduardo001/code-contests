// Read four integer values named A, B, C and D. Calculate and print the difference of product A and B by the product of C and D (A * B - C * D).

#include<bits/stdc++.h>
using namespace std;

int main() {
    int A, B, C, D, DIFERENCA;

    cin>>A;
    cin>>B;
    cin>>C;
    cin>>D;

    DIFERENCA = A * B - C * D;

    cout << "DIFERENCA = " << DIFERENCA << "\n";

    return 0;
}
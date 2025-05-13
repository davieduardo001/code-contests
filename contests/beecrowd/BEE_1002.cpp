#include <iostream>
#include <iomanip>
using namespace std;

#define PI 3.14159

int main() {
    double r, a;

    cin >> r;

    a = PI * (r*r);

    cout << "A=" << fixed << setprecision(4) << a << "\n";
    return 0;
}
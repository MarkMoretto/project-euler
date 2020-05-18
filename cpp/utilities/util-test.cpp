
#include <iostream>
#include "combiner.hpp"

const char nl = '\n';

int main() {
    int a = 2, b = 9;
    int res = Concat<int>(a, b);
    std::cout << "The combination of " << a << " and " << b << " is: " << res << "." << nl;
}
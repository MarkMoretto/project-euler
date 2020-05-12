
#include <iostream>
#include <vector>


const int M = 1e9 + 7; // Constant for large-number mod divider
const char nl = '\n';



constexpr int incr(int & n) {
    return ++n;
}

constexpr bool mod3(int & n) {
    return n % 3 == 0 ? true : false;
}

int main() {

    std::cout << "The value of M is: " << M << nl;

    return 0;
}
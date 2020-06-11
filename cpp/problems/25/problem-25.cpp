

#include <iostream>
#include <cmath>
#include <gmpxx.h>
// #include "MyFib.hpp"

using bigf = mpf_t;
using bigint = mpz_t;



bigint nth_fib(long& n) {
    bigf result;
    bigf lhs, rhs;

    bigf sqrt5 = std::sqrt(5);
    bigf rho = (1.0 + sqrt5) / 2.0;
    bigf psi = 1.0 - rho;


    result = (std::pow(rho, n) - std::pow(psi, n)) / sqrt5;
    return result;
}




int main() {
    long ntest=12;
    nth_fib f;

    std::cout << std::endl;
    
}
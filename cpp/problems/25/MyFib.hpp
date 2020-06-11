
// https://gmplib.org/manual/Initializing-Floats#Initializing-Floats

//https://www.learncpp.com/cpp-tutorial/132-function-template-instances/

// https://stackoverflow.com/questions/14126393/c-program-using-gmp-library

#ifndef H_FIB_TMPL_
#define H_FIB_TMPL_

#include <cmath>


template <class I, class F>
I nth_fib(long& n) {
    I result;
    F lhs, rhs;

    const double sqrt5 = std::sqrt(5);
    double rho = (1.0 + sqrt5) / 2.0;
    double psi = 1.0 - rho;

    lhs = std::pow(rho, n);
    rhs = std::pow(psi, n);
    result = std::floor((lhs - rhs) / sqrt5);
    return result;
}


#endif
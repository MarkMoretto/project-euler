
#include <iostream>
// #include <vector>
#include <algorithm>
#include <iterator>
#include "problem-401.h"

// Template should work for types representing non-negative integers

int main() {
    ll num(6), MOD;
    llvec v_worker;
    v_worker.reserve(num/2);

    ll b(10), e(9);
    MOD = Power(b, e);

    // Factors(num, v_worker);
    // for (auto &q : v_worker) 
    //     std::cout << q << std::endl;
    // std::cout << sum_of_squares(v_worker) << std::endl;
    std::cout << MOD << std::endl;

}

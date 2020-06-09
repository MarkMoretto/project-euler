/*
Header for counting number of digits in a positive integer value.

Template allows for type flexibility


TODO:
    modify to check for negative values
    modify to handle floating-point values

Example usage:

#include <iostream>
#include "number-length.hpp"

int main() {
    int testnum = 454545;
    unsigned res;
    res = digit_count(testnum);
    std::cout << "The number if digits in " << usr_num << " is " << res << nl;

}

*/

#pragma once

#ifndef _H_CNT_DIGIT_TMPL_
#define _H_CNT_DIGIT_TMPL_


// Base of the digits
// Can be adjusted for base 2, base 16, etc.
const int BASE = 10;


// Count number of digits in an integer
// General base should be 10
template<typename T>
T digit_count(T n) {

    unsigned int digit_count = 0;

    do {
        ++digit_count;
        n /= BASE;
    } while (n);

    return digit_count;
}


// Add two numeric values together
template<typename T>
T sum_two(T &x, T& y) {
    return x+y;
}



#endif
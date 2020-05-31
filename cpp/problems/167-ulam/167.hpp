#pragma once

#ifndef PE_167_ULAM_NUM_H_
#define PE_167_ULAM_NUM_H_

#include <cmath>
#include <iostream>
#include <vector>

// Newline constant
const char nl = '\n';


// https://en.cppreference.com/w/cpp/language/types
using ulng = unsigned long;
using ullng = unsigned long long;


// Unsigned vector
using uvec = std::vector<unsigned>;

// unsigned long long vector
using ullvec = std::vector<ullng>;


// First few ulam numbers for confirmation.
const std::vector<unsigned> ulam_actual{1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, 57, 62, 69, 72, 77, 82, 87, 97, 99, 102, 106, 114, 126, 131, 138, 145, 148, 155, 175, 177, 180, 182, 189, 197, 206, 209, 219, 221, 236, 238, 241, 243, 253, 258, 260, 273, 282, 282, 309, 316, 319, 324, 339};




inline bool is_prime(unsigned q) {

    if (q == 2) {
        return true;
    }

    if (q <= 1 || q % 2 == 0) {
        return false;
    }

    const unsigned n_max(std::sqrt(q));
    unsigned i;

    for (i= 0; i < n_max; i += 2) {
        if (q % i == 0) {
            return false;
        } 
        return true;
    }
}


// http://rosettacode.org/wiki/Ulam_spiral_(for_primes)#C.2B.2B
template<const unsigned SIZE>
class Ulam {
public:
    Ulam(ulng start = 1, )


private:

}



// template<typename T>
// T Concat(T& x, T& y) {
//     int factor = 1;
//     while (factor <= y) {
//         factor *= 10;
//     }
//     return factor * x + y;
// }



#endif
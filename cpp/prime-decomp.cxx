// Prime decomposition program
// Inspo: rosettacode.org/wiki/Prime_decomposition#C.2B.2B

// Compile note: Need to link to gmpxx.h location
// >>>g++ mycxxprog.cc -lgmpxx -lgmp

#include <iostream>
#include <vector>
#include <gmpxx.h>

// Template should work for types representing non-negative integers

template<typename Integer, typename OutputIterator>
void decompose(Integer n, OutputIterator out) {
    Integer i(2);

    while (n != 1) {
        while (n % i == Integer(0)) {
            *out++ = i;
            n /= i;
        }
        ++i;
    }
}



int main() {
    mpz_class number;

}
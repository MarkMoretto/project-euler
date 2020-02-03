/*
Project Euler

Problem: 3
Title: Largest prime factor
URI: https://projecteuler.net/problem=3
*/

#include <iostream>
#include <inttypes.h>

typedef std::intmax_t i_max; // Creating a type for the largest integer possible.
i_max target_value = 600851475143; // This is mostly here for output purposes.


int main() {
    i_max target_n = target_value;
    i_max *const p_target_n = &target_n;
    i_max a = 2;

    while (a * a <= *p_target_n) {
        if (*p_target_n % a == 0) {
            std::cout << a << "\n";
            *p_target_n /= a;
        }
        else {
            ++a;
        }
    }
    if (*p_target_n > 1) {
        std::cout << *p_target_n << std::endl;
    }

    std::cout << "The largest prime factor of " << target_value  << " is " << target_n << std::endl;

    return 0;
}


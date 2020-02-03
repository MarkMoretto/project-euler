/*
Project Euler

Problem: 16
Title: Power digit sum
URI: https://projecteuler.net/problem=16
*/

#include <iostream>
#include <vector>
#include <cmath>


using ld = long double;
typedef std::vector<ld> ldvec;

const char nl = '\n';

// void multiplier(ivec &v, int x) {
//     int tmp = 0;
//     int vsize = v.size();
//     for (int i = 0; i < vsize; i++) {
//         int res = tmp + v[i] * x;
        
//         v[i] = res % 10;
//         tmp = res / 10;
//     }
//     while (tmp != 0) {
//         v.push_back(tmp % 10);
//         tmp /= 10;
//     }
// }


double sum_pow_digits(int b, int e) {
    ldvec v;
    ld res = std::pow(b, e);

    // Populate vector
    while (res > 0) {
        double* tmp = new double[(int)&res];
        v.push_back(tmp % 10);
        res /= 10;
    }

    // Find sum of digits in vector
    ld tot(0);
    ld vsize = v.size();
    for (ld i = 0; i < vsize; i++) {
        tot += v[i];
    }
    return tot;
}

int main() {
    int base = 2;
    int expon = 1000;
    std::cout << base << " ^ " << expon << " = " << sum_pow_digits(base, expon) << std::endl;
    // ld res = std::pow(base, expon);
    // std::cout << base << " ^ " << expon << " = " << res << std::endl;
    return 0;
}
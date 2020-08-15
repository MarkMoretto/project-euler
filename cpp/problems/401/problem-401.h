
#ifndef PE_P401_H_
#define PE_P401_H_

#include <iostream>
#include <vector>

using ll = unsigned long long;
using ull = unsigned long long;
using llvec = std::vector<ll>;
using ullvec = std::vector<ull>;

ll MOD;

template <class N>
N Power(N base, N exponent) {
    N tot = 1;
    N * ptr_tot = &tot;
    N i;
    for (i = 0; i < exponent; i++) {
        *ptr_tot *= base;
    }
    return tot;

}

template <class Numeric>
void Factors(Numeric N, std::vector<Numeric>& vec) {
    Numeric i;

    vec.push_back(N);
    vec.push_back(1);

    for (i = 2; i * i <= N; ++i) {
        if (N % i == 0) {
            vec.push_back(i);
            if (i * i != N) { vec.push_back(N / i); }
        }
    }
}

template <class Numeric>
Numeric sum_of_squares(std::vector<Numeric>& vec) {
    Numeric tot(0);
    for (auto &q: vec) {
        tot += q*q;
    }
    return tot;
}

#endif
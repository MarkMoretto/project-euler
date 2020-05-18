
// Totient:
// http://rosettacode.org/wiki/Totient_function#C.2B.2B

// Productts: 
// https://stackoverflow.com/questions/5279051/how-can-i-create-cartesian-product-of-vector-of-vectors

#ifndef TOTIENT_FUNC_H_
#define TOTIENT_FUNC_H_

#include <iostream>
#include <vector>
#include <cassert>
#include <iomanip>


const char nl = '\n';

class totient_calculator {
    public:
        explicit totient_calculator(int max) : totient_(max + 1) {
            for (int i = 1; i <= max; ++i) {
                totient_[i] = i;
            }

            for (int i = 2; i <= max; ++i) {
                if (totient_[i] < i)
                    continue;
                for (int j = i; j <= max; j += i)
                    totient_[j] -= totient_[j] / i;
            }
        }
        int totient(int n) const {
            assert (n >= 1 && n < totient_.size());
            return totient_[n];
        }

        bool is_prime(int n) const {
            return totient(n) == n - 1;
        }
    private:
        std::vector<int> totient_;
};
 
int count_primes(const totient_calculator& tc, int min, int max) {
    int count = 0;
    for (int i = min; i <= max; ++i) {
        if (tc.is_prime(i))
            ++count;
    }
    return count;
}



#endif
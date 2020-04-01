
#include <iostream>
#include <cmath>
#include <vector>
#include <string>

const char nl = '\n';
using ulli = long long int;
using uvec = std::vector<ulli>;

uvec prime_factors(ulli n) {
    ulli t = 2;
    uvec outvec;

    while (pow(t, 2) <= n) {
        if (n % t == 0) {
            outvec.push_back(t);
            n /= t;
        } else {
            t++;
        }
    }
    if (n > 1) {
        outvec.push_back(n);
    }
    return outvec;
}


int main() {
    ulli test1 = 90;
    ulli* p_t = &test1;
    uvec res;
    std::string out_s = "";
    res = prime_factors(test1);
    res.shrink_to_fit();
    std::cout << "The prime factors of " << test1 << "are: " << nl;
    for (auto &q : res) {
        out_s += q + ", ";
    }
    std::cout  << out_s << nl;
    return 0;
}

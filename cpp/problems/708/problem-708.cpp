// Working on projecteuler.com question 708.
// URL: https://projecteuler.net/problem=708

#include <iostream>
#include <vector>
#include <numeric>

using uint = std::uint64_t;
using ivec = std::vector<uint>;
const char nl = '\n';
const uint zero = 0;
const uint uone = 1;
const uint utwo = 2;



void decompose(uint n, ivec &v) {
    // Prime decomposition of a number.
    uint i = 2;

    // In addition we define f(1)=1.
    while (n != 1) {
        while (n % i == zero) {
            // v.push_back(i);
            v.push_back(utwo);
            n /= i;
        }
        ++i;
    }
}


void product(uint &n, ivec *v) {
    n = 1;
    for (uint &i : *v) {
        n *= i;
    }  
}

uint f(uint n) {
    
    ivec v1;
    ivec* ptr_v = &v1;
    uint prod;

    decompose(n, v1);
    v1.shrink_to_fit();

    product(prod, ptr_v);
    return prod;
}

uint S(uint N) {
    std::cout << "N value: " << N << nl;

    ivec vN;
    vN.reserve(N + uone);

    std::cout << "Capacity of vN: " << vN.capacity() << nl;

    uint f_res = zero;

    std::iota(std::begin(vN), std::end(vN), 1);

    std::cout << "Size of vN: " << vN.size() << nl;




    for (auto &x : vN) {
        uint tmp = f(x);
        if (tmp > 0) {
            f_res += tmp;
        }
    }

    return f_res;

}

// void Testf();
void TestS();
int main() {

    // uint testN = 1000;
    // uint result;

    // result = S(testN);
    // std::cout << "The result of S(N) with an N value of " << testN << " is: " << result << nl;

    // Testf();
    TestS();

    return 0;
}

void Testf() {
    uint n1 = 90;
    uint result;
    result = f(n1);
    std::cout << "The result of f(n) with n of " << n1 << " is: " << result << nl;
}

void TestS() {
    uint n1 = 90;
    uint result;
    result = S(n1);
    std::cout << "The result of S(N) with n of " << n1 << " is: " << result << nl;
}


void PrintSample(uint *n, ivec *v) {
    std::cout << "The prime factors of " << *n << " are:" << nl;
    for (uint &i : *v) {
        std::cout << i << nl;
    }
}
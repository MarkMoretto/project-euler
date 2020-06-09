/**
 * Title: 1000-digit Fibonacci number
 * URL: https://projecteuler.net/problem=25
*/


#include <iostream>
// #include <vector>
#include "p25.hpp"


const char nl = '\n';
using ll = long long int;

void nth_fib(int &MAX_N, ll & ncount) {
    ll fib, a, b;
    a = 0;
    b = 1;

    // Increment counter by 1
    ncount++;

    do {
        fib = sum_two(a, b);
        ncount++;
        a = b;
        b = fib;
    } while (digit_count(fib) < MAX_N); 
}



int main() {
    int N = 30;
    ll fibth = 0;

    nth_fib(N, fibth);

    std::cout << "Term " << fibth << " is the first term to contain " << N << " digits." << nl;

    return 0;
}



// ll vec_sum(std::vector<ll>& v) {
//     for (auto& i : v)
// }
// void fib(int &N, std::vector<ll>& v) {
//     ll a = 1;
//     ll b = 1;
//     int curr_max;
//     ll arr_sum;


//     v.push_back(0);
//     v.push_back(1);
//     arr_sum = 1;
//     while (digit_count(vec_sum) < N) {
//         ll fib = 0;
//         for (auto& i : v)
//             fib += i;

//         v.erase(v.begin());
//     }

//     for(unsigned int n = 3; n <= target; ++n)
//     {
//             unsigned int fib = a + b;
//             std::cout << "F("<< n << ") = " << fib << std::endl;
//             a = b;
//             b = fib;
//     }    
// }
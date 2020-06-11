
// g++ -std=c++17 -Wall -Wextra problems\problem-127\main.cpp -o problems\p127

// cd problems\problem-127
// g++ -std=c++17 -Wall -Wextra main.cpp -o p127
#include <iostream>
#include <algorithm> // std::__gcd(), std::sort(), std::unique()
#include <vector> // std:: vector
#include <array> // std::array
#include <numeric> // std::iota()
#include "p127-utils.hpp" // remove_duplicates(), vproduct()



void unique_prime_factors(long num, lvec& v) {
    //long maxval = *std::max_element(std::begin(v), std::end(v));
    v.reserve(num);

    for (long i = 2; i <= num; i++) {
        while (num % i == 0) {
            v.push_back(i);
            num /= i;
        }
    }

    // From p127-utils.hpp
    remove_duplicates(v);
}



long rad(lvec& vec) {
    // Compute product of prime facctors
    long out, prod;
    lvec tmpv;

    prod = vproduct(vec);

    // Popualte tmpv with unique prime factors
    unique_prime_factors(prod, tmpv);
    
    // Find and return the product of tmpv.
    out = vproduct(tmpv);
    return out;
}


template <class T>
bool gcd_check(T& x, T& y, T& z) {
    // Check if gcd(a,b) == gcd (a, c) == gcd(b, c) == 1;
    if (std::__gcd(x, y) == 1 && std::__gcd(x, z) == 1 && std::__gcd(y, z) == 1) {
        return true;
    }
    return false;
}


template <class T, class V>
void descending_range(T start, V& vec) {
    // Popualte vector with descending range.
    // Params are start and vector reference.
    for (T i = start; i > 0; --i) {
        vec.push_back(i);
    }
}


template <class T, class V>
void ascending_range(T end, V& vec) {
    // Popualte vector with ascending range.
    // Params are end and vector reference.    
    for (T i = 0; i < end; i++) {
        vec.push_back(i);
    }
}


template <class T, class V>
void asc_range_start(T start, T end, V& vec) {
    // Popualte vector with ascending range.
    // Params are start, end, and vector reference.    
    for (T i = start; i < end; i++) {
        vec.push_back(i);
    }
}


int main() {
    long N = 1000;
    


    lvec a_vec, b_vec, c_vec, results;
    results.reserve(N);

    // Set a vector values (ascending)
    ascending_range(N, a_vec);
    ascending_range(N, b_vec);


    // Set c vector values (descending)
    descending_range(N - 1, c_vec);

    for (long &c : c_vec) {
        //std::cout << c << nl;
        for (long &a : a_vec) {
            // Set b vector values (ascending).
            // Will start from current value of a.
            // asc_range_start(a, N, b_vec);

            for (long &b : b_vec) {
                if (a < b) {

                    lvec tempv{a, b, c};
                    long rad_res = rad(tempv);                
                    if (gcd_check(a, b, c) == true && (a + b) == c && rad_res < c) {

                        std::cout << a << ws << b << ws << c << ws <<  rad_res << nl;
                        results.push_back(c);
                        
                    }
                }
            }
        }
    }



    long result_sum = 0;
    for (long &r : results) {
        result_sum += r;
        std::cout << r << ws;
    }

    std::cout << nl << "The `abc-hits` sum for c < " << N << " is: " << result_sum<< nl;
    
}

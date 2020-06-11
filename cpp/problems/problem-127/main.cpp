
// g++ -std=c++17 -Wall -Wextra problems\problem-127\main.cpp -o problems\p127

// cd problems\problem-127
// g++ -std=c++17 -Wall -Wextra main.cpp -o2 -o p127

#include <iostream>
#include <algorithm> // std::__gcd(), std::sort(), std::unique()
#include <vector> // std:: vector
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




int main() {

    const long N = 1000;
    long C_start = N -1;

    // lvec a_vec, b_vec, c_vec;
    long a, b, c;
    lvec results;
    results.reserve(N);


    for ( c = C_start; c > 0; --c ) {
        for ( a = 0; a < N; ++a ) {
            long b_start = a + 1;
            for ( b = b_start; b < N; b++ ) {
                lvec tempv{a, b, c};
                long rad_res = rad(tempv);
                if (gcd_check(a, b, c) == true && (a + b) == c && rad_res < c) {
                    std::cout << a << ws << b << ws << c << ws <<  rad_res << nl;
                    results.push_back(c);
                    continue;
                }
            }
        }
    }

    // // Set a vector values (ascending)
    // ascending_range(N, a_vec);
    // ascending_range(N, b_vec);

    // // Set c vector values (descending)
    // descending_range(N - 1, c_vec);

    // for (long &c : c_vec) {
    //     //std::cout << c << nl;
    //     for (long &a : a_vec) {
    //         // Set b vector values (ascending).
    //         // Will start from current value of a.
    //         // asc_range_start(a, N, b_vec);

    //         for (long &b : b_vec) {
    //             if (a < b) {

    //                 lvec tempv{a, b, c};
    //                 long rad_res = rad(tempv);                
    //                 if (gcd_check(a, b, c) == true && (a + b) == c && rad_res < c) {

    //                     std::cout << a << ws << b << ws << c << ws <<  rad_res << nl;
    //                     results.push_back(c);
    //                     results.
                        
    //                 }
    //             }
    //         }
    //     }
    // }



    long result_sum = 0;
    for (long &r : results) {
        result_sum += r;
        std::cout << r << ws;
    }

    std::cout << nl << "The `abc-hits` sum for c < " << N << " is: " << result_sum<< nl;
    
}

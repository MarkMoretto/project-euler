/*
Project-Euler

Problem number: 7
Title: 10001st Prime
URI: https://projecteuler.net/problem=7
*/

#include <iostream>
#include <vector>
#include <sstream>


const char nl = '\n';
using ivec = std::vector<int>;

void primes(ivec& v, int max_n) {

    int i = 3;
    int vec_size;
    v.push_back(2);

    while (true) {

        bool is_prime = true;

        for (auto &q : v) {

            if (i % q == 0) {
                is_prime = false;
                break;
            }
        }

        if (is_prime) {
            v.push_back(i);
        }

        vec_size = v.size();
        if (vec_size == max_n) {
            break;
        }
        i++;
    }

}


int main() {
    std::ostringstream oss;
    int target_count = 10001;
    ivec results;
    results.reserve(target_count * 2);

    primes(results, target_count);

    // oss << nl << "The first " <<  target_count << " prime numbers are:" << nl;
    // for (auto &q : results) {
    //     oss << q << nl;
    // }
    oss << nl << "The last prime number in the set is: " << results.back() << nl;
    std::cout << oss.str();

    

    return 0;
}

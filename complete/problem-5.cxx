/*
Project Euler

Problem: 5
Title: Smallest multiple
URI: https://projecteuler.net/problem=5
*/

#include <iostream>
#include <numeric>
#include <vector>

typedef std::vector<std::uint64_t> int_vec;

int main() {
    std::uint64_t max_n = 20;
    std::uint64_t n = 0;
    std::uint64_t counter = 0;
    int_vec v(max_n);
    std::iota(v.begin(), v.end(), 1);
    bool match = false;
    while (!match) {
        counter = 0;
        ++n;
        for (auto &y : v) {
            if (n % y == 0) {
                counter++;
            }
        }
        if (counter == max_n) {
            match = true;
        }
    }
    std::cout << "The smallest number that can be divided by each of the numbers from 1 to 20 is: " << n << "\n";
    return 0;
}

/*
Project Euler

Problem: 4
Title: Largest palindrome product
URI: https://projecteuler.net/problem=4
*/

#include <iostream>
#include <numeric>
#include <algorithm>
#include <vector>
#include <string>


typedef std::vector<int> int_vec;


int main() {

    int current_max = 0, res;
    int_vec v(999);
    std::iota(v.begin(), v.end(), 1);

    std::string s1;

    for (auto &y : v) {
        for (auto &x : v) {
            res = x * y;
            s1 = std::to_string(res);
            std::string rs1(s1.rbegin(), s1.rend());
            if (s1 == rs1) {
                std::cout << x << " " << y << " " << res << std::endl;
                if (res > current_max) {
                    current_max = res;
                }
            }
        }
    }
    std::cout << "The max palindrome for two 2-digit numbers is: " << current_max << "\n";

    return 0;
}

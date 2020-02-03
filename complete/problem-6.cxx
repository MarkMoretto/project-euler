/*
Project Euler

Problem: 6
Title: Sum square difference
URI: https://projecteuler.net/problem=6
*/

#include <iostream>
#include <numeric>


void sumsquare(int n, int& res) {
    for (int i = 1; i <= n; ++i) {
        res += i * i;
    }
}


void squaresum(int n, int& res) {
    int tmp = 0;
    for (int i = 1; i <= n; ++i) {
        tmp += i;
    }
    res = tmp * tmp;
}


int main() {
    int target(100);
    int res1 = 0, res2 = 0;
    int output;
    
    sumsquare(target, res1);
    squaresum(target, res2);
    std::cout << "sumsquare: " << res1 << ", squaresum: " << res2 << std::endl;
    output = res2 - res1;
    std::cout << "Result: " << output << std::endl;
    return 0;
}


/*
Project Euler

Problem: 20
Title: Factorial digit sum
URI: https://projecteuler.net/problem=20
*/

#include <iostream>
#include <stack> 
#include <vector>

typedef std::vector<int> ivec;

void multiplier(ivec &v, int x) {
    int tmp = 0;
    int vsize = v.size();
    for (int i = 0; i < vsize; i++) {
        int res = tmp + v[i] * x;
        
        v[i] = res % 10;
        tmp = res / 10;
    }
    while (tmp != 0) {
        v.push_back(tmp % 10);
        tmp /= 10;
    }
}

int sum_digits(int n) {
    ivec v;

    v.push_back(1);

    for (int i = 1; i <= n; i++) {
        multiplier(v, i);
    }

    // Find sum of digits in vector
    int tot(0);
    int vsize = v.size();
    for (int i = 0; i < vsize; i++) {
        tot += v[i];
    }
    return tot;
}

int main() {
    int to_eval = 100;
    std::cout << "The sum of the digits in " << to_eval << "! is: "  << sum_digits(to_eval)  << std::endl;
    return 0;
}


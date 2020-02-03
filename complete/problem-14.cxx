/*
Project Euler

Problem: 14
Title: Longest Collatz sequence
URI: https://projecteuler.net/problem=14
*/

#include <iostream>
#include <vector>

const char nl = '\n';
const long max_N = 1000000;



void evencalc(long& x) {
    x /= 2;
}


void oddcalc(long& x) {
    x *= 3;
    x += 1;
}


void testfunc() {
    long n = 837799;
    long counter = 1;
    while (n > 1) {
        ++counter;
        n % 2 == 0 ? evencalc(n) : oddcalc(n);
        
        std::cout << "Current value of n: " << n << nl;
    }
    std::cout << "The number of values found for 837799 is " << counter << nl;
}

// void testfunc();
int main() {
    int counter;
    int start = 1;
    int largest = 0;
    int best_start = 0;

    while (start < max_N) {
        counter = 1;
        long n2 = start;
        while (n2 > 1) {
            ++counter;
            n2 % 2 == 0 ? evencalc(n2) : oddcalc(n2);
        }
        if (counter > largest) {
            largest = counter;
            best_start = start;
            // std::cout << "Current:\n\tlongest Collatz sequence: " << largest <<"\n\tBest start: " << best_start << nl;
        }
        start += 1;
    }
    std::cout << "\nThe starting number which produces the longest Collatz sequence for numbers up to 1 million is " << best_start << nl;
    std::cout << "The number of values in the longest string was: " << largest << nl;

    return 0;
}


// void testfunc() {
//     long n = 13;
//     long counter = 1;
//     while (n > 1) {
//         ++counter;
//         n % 2 == 0 ? evencalc(n) : oddcalc(n);
        
//         std::cout << "Current value of n: " << n << nl;
//     }
//     std::cout << "The number of values found for 837799 is " << counter << nl;
// }

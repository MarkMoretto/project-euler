/*
Project Euler

Problem: 2
Title: Even Fibonacci numbers
URI: https://projecteuler.net/problem=2
*/

#include <iostream>

int main() {
        int n1 = 0;
        int n2 = 1;
        int current = 0;
        int tot = 0;
        int max_n = 4000000;

        while (current < max_n) {
            if (current % 2 == 0) {
                std::cout << current << "\n";
                tot += current;
            }
            current = n1 + n2;
            n1 = n2;
            n2 = current;

        }
        std::cout << "The total is: " << tot << std::endl;
        return 0; 

}
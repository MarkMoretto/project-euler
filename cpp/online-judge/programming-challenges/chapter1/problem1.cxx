/* 
Online Judge - Programming Challenges
Chapter 1
100 - The 3n + 1 problem
online-judge\programming-challenges\chapter1\problem1.cxx

Reference:
https://onlinejudge.org/data/p100.c.html
*/

#include <iostream>
#include <stdio.h>


void cycler(int n, int &counter) {
    while (n > 1) {
        counter += 1;
        n % 2 > 0 ? n = (n * 3) + 1 : n /= 2;
    }
    counter += 1;
}


void find_max_cycle(int n_max, int n_min, int &solution) {
    int N, counts;
    solution = -1; // Initial solution should be negative.
    for (N = n_min; N <= n_max; N++) {
        counts = 0; // Reset counds to zero.
        cycler(N, counts);
        if (counts > solution) {
            solution = counts;
        }
    }
}


template <class NUM>
void hotswap(NUM &x, NUM &y) {
    NUM tmp;
    if (x > y){
        tmp = x;
        x = y;
        y = tmp;
    }    
}



int main() {

    int i;
    int j;
    int iOriginal;
    int jOriginal;


    // int tmp;
    int result; // Cumulative number of valid digits used in calculation.

    while (scanf("%d %d\n", &i, &j)==2) {
        iOriginal = i;
        jOriginal = j;
        
        hotswap(i, j);

        find_max_cycle(j, i, result);
        std::cout << iOriginal << " " << jOriginal << " " << result << std::endl;        
    }

    return 0;
}
// g++ -Wall -Wextra -o p1 problem1.cxx


// void test_solution(int start, int stop, int &out) {
//     int i;
//     int j;
//     int iOriginal;
//     int jOriginal;
//     int result;

//     std::cout << "Please enter two numbers: " << std::endl;

//     if (scanf("%d %d", &i, &j)==2) {
//         iOriginal = i;
//         jOriginal = j;
//         hotswap(i, j);
//         find_max_cycle(j, i, result);

//         std::cout << iOriginal << " " << jOriginal << " " << result << std::endl;
//     }
// }
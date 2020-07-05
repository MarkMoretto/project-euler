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


void solution(int start, int stop, int &counter) {
    int * ss = &start;
    int * sp = &stop;
    while (*ss > *sp) {
        counter += 1;
        *ss % 2 > 0 ? *ss = (*ss * 3) + 1 : *ss /= 2;
    }
    counter += 1;
}

int main() {
    int i, j; // Start
    int iOriginal, jOriginal;
    int tmp;
    int total; // Cumulative number of valid digits used in calculation.

    while (scanf("%d %d\n", &i, &j)==2) {
        iOriginal = i;
        jOriginal = j;

        /* swap if out of order */
        // if (i > j){
        //     tmp = i;
        //     i = j;
        //     j = tmp;
        // }

        solution(j, i, total);
        std::cout << iOriginal << " " << jOriginal << " " << total << std::endl;        
    }
    return 0;
}

// void test_solution(int start, int stop, int &out) {
//     int * ss = &start;
//     int * sp = &stop;

//     while (*ss > *sp) {
//         std::cout << *ss << " ";
//         out += 1;
//         *ss % 2 > 0 ? *ss = (*ss * 3) + 1 : *ss /= 2;
//     }
    
//     out += 1;
//     std::cout << *sp << std::endl;
// }
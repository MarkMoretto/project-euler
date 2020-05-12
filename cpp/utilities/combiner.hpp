// https://www.daniweb.com/programming/software-development/threads/425472/how-concatenate-number-in-c

#ifndef CONCAT_INT_UTIL_H_
#define CONCAT_INT_UTIL_H_

#include <iostream>

template<typename T>
T Concat(T& x, T& y) {
    int factor = 1;
    while (factor <= y) {
        factor *= 10;
    }
    return factor * x + y;
}


// int concat(int a, int b) {
//     int magnitude = 1;
//     while(magnitude <= b) magnitude *= 10;
//     return magnitude * a + b;
// }

// int main() {
//     int a=99,b=10;
//     cout << together(a,b) << endl;
//     return 0;
// }


#endif
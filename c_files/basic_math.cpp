
#include <stdio.h>
#include "basic_math.h"


int SumInt(int a, int b) {
    return (a + b);
}


int Abs(int n) {
    if (n < 0) {
        return (n * -1);
    } else {
        return n;
    }
}

float Absf(float n) {
    if (n < 0.0) {
        return (n * -1.0);
    } else {
        return n;
    }
}
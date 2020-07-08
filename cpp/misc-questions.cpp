// Used to pass LinkedIn C++ assessment.
#include <iostream>
#include <vector>
#include <stdbool.h>
#include <cstdio>

// g++ -Wall -Wextra -o miscq misc-questions.cpp
using namespace std;

int mystrcpy(char * dest, char *orig) {
    int count = 0;
    while (*orig != '\0') {
        *dest++ = *orig++;
        count++;
    }
    *dest = *orig;
    return count;
}


int main() {

    printf("1/2 = %f", (float)(1/2));

    return(0);
}

// Chapter 1.6 - Arrays

#include <stdio.h>


int main() {
    int c;
    int i;
    int nwhite;
    int nother;
    int ndigit[10];

    nwhite = nother = 0;

    // Fill ndigit with zeroes.
    for (i = 0; i < 10; ++i) {
        ndigit[i] = 0;
    }

    // If reading file input.
    // Requires input to run.
    while ((c = getchar()) != EOF) {
        if (c >= '0' && c <= '9') {
            ++ndigit[c-'0'];
        }  else if (c == ' ' || c == '\n' || c == '\t') {
            ++nwhite;
        } else {
            ++nother;
        }
    }

    printf("digits = ");
    for (i = 0; i < 10; ++i) {
        printf(" %d", ndigit[i]);
    }
    printf(", whitespace = %d, other = %d\n", nwhite, nother);

}
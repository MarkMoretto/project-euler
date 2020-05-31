/**
 * Print Fahrenheit and Celsius temperatures.
 * 
 * Note: Temperature may be referred to as temp in this script, but it does not mean temporary.
*/

#include <stdio.h>


int main() {
    int fahr, celsius;
    int lower, upper, step;

    lower = 0;      // Lower limit of temp table
    upper = 300;    // Upper bound of temp table
    step = 20;      // Temperature step size.

    fahr = lower;
    printf("F\tC\n");
    printf("------------\n");
    while (fahr <= upper) {
        celsius = 5 * (fahr - 32) / 9;
        printf("%d\t%d\n", fahr, celsius);
        fahr += step;
    }
}


#include <iostream>
#include <vector>
#include <stdbool.h>



int main() {
    
    return 0;
}

int mystrcpy(char * dest, char *orig) {
    int count = 0;
    while (*orig != '\0') {
        *dest++ = *orig++;
        count++;
    }
    *dest = *orig;
    return count;
}
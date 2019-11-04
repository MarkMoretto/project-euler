// data\problem_8_data.txt
#include <stdio.h>



int main() {
    FILE *fptr;
    char fpath[] = "C:\\Users\\Work1\\Desktop\\Info\\PythonFiles\\project-euler\\data\\problem_8_data.txt";
    if ((fptr = fopen(fpath, "r")) == NULL) {
        printf("Error opening data file!");
        exit(1);
    }
}
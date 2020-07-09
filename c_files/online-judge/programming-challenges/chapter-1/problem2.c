
/**
 * 
 * 
 * Relative folder path: online-judge\programming-challenges\chapter-1
*/

#include <stdio.h>

const unsigned int buff_size = 255;


void read_file(const char *fp) {
    FILE * f_ptr;
    char buffer[buff_size];

    f_ptr = fopen64(fp, "r");

    while (fgets(buffer, buff_size, f_ptr)) {
        printf("%s", buffer);
    }
}


int main(int argc, char ** argv) {

    const char *filepath = NULL;

    if(argc == 2) {

        filepath = argv[1];

        read_file(filepath);    

    } else {
        
        printf("One argument expected.\n");

    } 


}

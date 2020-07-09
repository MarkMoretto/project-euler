
#ifndef FILEREADER_H_
#define FILEREADER_H_

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


const unsigned int buffer_size = 255;
char buffer[buffer_size];


int read_lines(const char *fp) {
    int i, j;
    int ALLOC_LINES = 128;
    int LINE_LENGTH = 100;
    // Creaet line buffer
    char **line = (char**)malloc(sizeof(char*) * ALLOC_LINES);
    if (line == NULL) {
        fprintf(stderr, "Memory error (1)\n");
        return 1;
        }

    FILE * f_ptr = fopen(fp, "r");
    if (f_ptr == NULL) { return 2; }

    for (i=0;;i++) {
        if (i >= ALLOC_LINES) {
            // Add more room to lines.

            int line_resize = ALLOC_LINES * 2;
            line = (char**)realloc(line, sizeof(char*) * line_resize);

            if (line == NULL) {
                fprintf(stderr, "Realloc memory error (3)\n");
                return 3;
            }
            ALLOC_LINES = line_resize;
        }

        // Allocate space for next line
        line[i] = malloc(LINE_LENGTH);
        if (line == NULL) {
            fprintf(stderr,"Out of memory (3).\n");
            exit(4);
        }
        if (fgets(line[i], LINE_LENGTH-1, f_ptr)==NULL) { break; }

        for (j = strlen(line[i])-1;j>=0 && (line[i][j]=='\n' || line[i][j]=='\r'); j--);
        line[i][j+1]='\0';
    }

    fclose(f_ptr);
    for (j=0;j<i;j++) printf("%s\n", line[j]);

    for (; i>=0; i--) free(line[i]);
    free(line);
    return 0;
}


int read_file(const char *fp) {

    FILE * f_ptr = fopen(fp, "r");
    if (f_ptr == NULL) { return 2; }
    while (fgets(buffer, buffer_size, f_ptr)) {
        printf("%s", buffer);
    }
}

#endif
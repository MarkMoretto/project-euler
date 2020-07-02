// https://stackoverflow.com/questions/62687952/how-to-pass-2-d-char-array-to-a-function#62688115

#include <iostream>


const int r = 6;
const int c = 7;


void final_output(char arr) {
    for(int i = 0; i < r; i++){
        for(int j = 0; j < c; j++){
            std::cout << arr[i][j];
        }
    }
}


int main() {
    char x[r][c] = { 0 };

    final_output(x);


    return 0;
}

// https://www.programiz.com/cpp-programming/multidimensional-arrays
// Multidimensional array practice

#include <iostream>


int main() {

    // Using non-traditional rows, cols vs. i, j for clarity.
    int rows, cols;
    rows = 3;
    cols = 2;

    int test[rows][cols] = {
        {2, -5},
        {4, 0},
        {9, 1}
    };

    for (int r = 0; r < rows; ++r) {
        for (int c = 0; c < cols; ++c) {
            std::cout << "test[" << r << "][" << c << "] = " << test[r][c] << std::endl;
        }
    }
    return 0;
}

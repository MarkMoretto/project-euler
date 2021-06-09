// https://stackoverflow.com/questions/67896401/what-do-i-get-wrong-output-random-numbers-in-my-output-in-vscode#67896426

#include <iostream>

int main() {
    int A[5];
    int i;
    for (i = 0; i < 5; i++) {
        std::cin >> A[i];
    }
    std::cout << sizeof(A) << std::endl;

    for (i = 4; i>=0; i--) {
        std::cout << A[i] << " ";
    }
    return 0;
}

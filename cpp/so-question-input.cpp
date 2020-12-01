// https://stackoverflow.com/questions/65067169/after-trying-to-run-this-simple-code-i-can-only-type-in-value-once-why

#include <iostream>


int main() {
    // char * str = new char[10];
    // std::cin.get(str, sizeof(*str));

    char * strline = new char[10];
    std::cin.getline(strline, sizeof(strline));
    std::cout << "Your input: " + (std::string)strline << std::endl;
    return 0;
}


#include <iostream>
#include <regex>

#include "input-conversion.hpp"

const char nl = '\n';

// void tester() {
//     IntVec dimv, arrv, consv;

//     // Strings to hold user input values.
//     STRING inputs;

//     std::cout << "Welcome to the Program!" << nl << nl;
//     std::cout << "When prompted, please enter all values with a single space inbetween them." << nl << nl;

//     std::cout << "Enter array size and number of consecutive values: " << nl;
//     getline(std::cin, inputs);

//     arrv = string_to_int(inputs);      
// }

void regex_test_1();

int main() {
    regex_test_1();

}

void regex_test_1() {
    // Sample data for testing regular expressions
    STRING sample_input = "1,2, 3|||6  &9";

    STRING no_digits_pattern = "([\\D]+)";
    STRING ws_replacement = " ";

    // Init regex constructor
    std::regex ptrn (no_digits_pattern);

    std::cout << std::regex_replace(sample_input, ptrn, ws_replacement);    
}
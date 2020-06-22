/**
 * Header for printing info to command prompt.
 * 
*/


#include <iostream>
#include <sstream>
#include <vector>



/**************************************************************
 * Clear stringstream.
*/
void reset_ss(std::stringstream &s) {
    s.str(std::string()); // Clear stringstream.
    s.clear(); // Clear any errors
}


/**************************************************************
 * Print each line of generated permutation to standard output.
*/
template <typename T>
void print_vec(std::vector<T> &vec) {

    std::stringstream ss; // Stringstream object.
    int v_sz = vec.size()-1; // Max size of vector, less 1 spot.

    for (int i = 0; i <= v_sz; i++) {
        if (i < v_sz) {
            ss << vec[i] << ",";
        } else {
            ss << vec[i];
        }
    }
    std::cout << "(" << ss.str() << ")" << nl; // Write stringstream to console.
    reset_ss(ss);    
}
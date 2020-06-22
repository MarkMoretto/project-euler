



#include <iostream>
#include <algorithm> // std::next_permutation, std::sort
#include <vector>
#include <sstream>


const int N = 3;
const char nl = '\n';


/**************************************************************
 * Populate vetor with ascending numbers.
 * Includes options `start` param.
*/
template <typename Q, typename T>
void populate_vec(Q n, std::vector<T> &v, Q start = 1) {
    for (Q i = start; i <= n; i++) {
        v.push_back(i);
    }
}

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

/**
 * 
*/
template <class Q>
void append_two(std::vector<Q> &vec, int n_values=2) {
    Q tmp;
    for (int i = 0; i < n_values; i++) {
        tmp = vec[i];
        vec.push_back(tmp);
    }
}

int main() {
    std::vector<int> v;
    int found_index;
    v.reserve(N+2);// Allocate some space to the vector.
    populate_vec(N, v); // Populate vecotr with numbers ranging from 1 to N.

    std::sort(v.begin(), v.end()); // Sort vector

    do {
        // print_vec(v);
        int step = N - 2;
        int loopmax = v.size() - step; // Adjusted top-end of for loop

        int * idx = &found_index;
        *idx = 0; // Seed idx with initial value.

        append_two(v);
        for (int z=0; z < loopmax; z++) {
            if ((v[z] < v[z+1]) && (v[z+1] < v[z+2])) {
                *idx = z+1;
                break;
            }
            if (*idx>0) 
                break;
            
        }

    } while(std::next_permutation(v.begin(), v.end()));

    std::cout << "Condition met at index: " << found_index << nl;

    return 0;
}


/**
 * Description: Header for utilities used in project-euler problem 127
 * 
*/


#ifndef H_P127_UTILS_
#define H_P127_UTILS_

#include <vector>
#include <algorithm>


// User-defined constants
const char ws = ' ';
const char nl = '\n';


// User-defined types
using ivec = std::vector<int>;
using lvec = std::vector<long>;


// Remove duplicate values from vector
template <typename T>
void remove_duplicates(T& v) {
    // Sort
    std::sort(v.begin(), v.end());

    // Reduce
    auto uniq = std::unique(v.begin(), v.end());

    // Compact
    v.erase(uniq, v.end());
}


// Product of vector values (or arrays, if v >= C++11 used)
template <typename NUM>
long vproduct(NUM& v) {
    // Start at 1 since 0 will return 0 after multiplication.
    long out = 1;

    for (auto &i : v) {
        out *= i;
    }

    return out;
}



// Populating of vectors/arrays
/**
 * 
*/
template <class T, class V>
void descending_range(T start, V& vec) {
    // Popualte vector with descending range.
    // Params are start and vector reference.
    for (T i = start; i > 0; --i) {
        vec.push_back(i);
    }
}


template <class T, class V>
void ascending_range(T end, V& vec) {
    // Popualte vector with ascending range.
    // Params are end and vector reference.    
    for (T i = 0; i < end; i++) {
        vec.push_back(i);
    }
}


template <class T, class V>
void asc_range_start(T start, T end, V& vec) {
    // Popualte vector with ascending range.
    // Params are start, end, and vector reference.    
    for (T i = start; i < end; i++) {
        vec.push_back(i);
    }
}

#endif
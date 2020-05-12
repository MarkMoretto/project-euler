// https://ideone.com/86h2wn
// https://www.cplusplus.com/reference/algorithm/next_permutation/

#ifndef PERM_UTIL_H_
#define PERM_UTIL_H_

#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>


const char nl = '\n';

template <typename T>
void Permutations(std::vector<T> v, std::vector<T> &outv) {
    std::sort(v.begin(), v.end());
    do {
        std::copy(v.begin(), v.end(), std::ostream_iterator<T>(std::cout, " "));
        std::cout << nl;
    } while (std::next_permutation(v.begin(), v.end()));
}



#endif
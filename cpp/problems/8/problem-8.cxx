
#include <iostream>
#include <vector>

#include "problem-8.hpp"

// template <typename T>
constexpr int CHUNKSIZE = 4;


void set_vector(ivec & v) {
    int lng_sz = sizeof(LONG_NUMBER);
    v.reserve(lng_sz);
    for (int i = 0; i < lng_sz; i++) {
        int tmp_ = LONG_NUMBER[i];
        v.push_back(tmp_);
    }
}


int product(ivec & iv) {
    int res = 1;
    for (int &i : iv) {
        res *= i;
    }
    return res;
}


int main() {
    ivec vc, top_vec;
    int max_product = -1;

    set_vector(vc);
    
    std::cout << "The first 10 elements in the converted vector are:" << std::endl;
    for (int i; i < 10; i++) {
        char ch_vc = vc[i];
        std::cout << " " << (int)ch_vc;
    }

    // int max_n = vc.size() - CHUNKSIZE;

    // for (int i=0; i < max_n; i++) {
    //     ivec tempvec(&vc[i], &vc[i + CHUNKSIZE]);
    //     int prod = product(tempvec);
    //     if (prod > max_product) {
    //         max_product = prod;
    //         top_vec = tempvec;
    //     }
    // }
    // std::cout << "The top product value was " << max_product << " for:" << std::endl;
    // for (int & ix : top_vec) {
    //     std::cout << " " << ix;
    // }
    // std::cout << std::endl;

}



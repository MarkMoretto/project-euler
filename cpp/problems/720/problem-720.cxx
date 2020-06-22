/**
 * Project euler problem 720
 * https://projecteuler.net/problem=720
*/

#include <iostream>
#include <algorithm> // std::next_permutation, std::sort
#include <vector>
#include "p720.hh"


using namespace FuncUtil;

const long N = 4;


/**
 * Evalute chunks of vector elements
*/
template <typename VecNumType>
long eval_three(std::vector<VecNumType> vec) {
    long idx=0;
    VecNumType *v_ptr = &vec;
    append_two(*v_ptr); // Add first two elements to end of vector.

    //int maxsize = *v_ptr.size()-2;


    for (int n = 0; n < *v_ptr.size(); n++) {

        if VMn(vec[n], vec[n+1], vec[n+2]) {

            idx = n+1;
            break;
        }
    }
    return idx;  
}

int main() {
    lvec coreV;
    coreV.reserve(N);
    populator(N, coreV);
    std::sort(coreV.begin(), coreV.end());

    do {
        


    } while (std::next_permutation(coreV.begin(), coreV.end()));









    return 0;
}


#ifndef PE_P720_H_
#define PE_P720_H_

#include <iostream>
#include <vector>

namespace FuncUtil {

    // Using types
    using ll = long long;
    using ull = unsigned long long;

    using lvec = std::vector<long>; // Long vector
    using llvec = std::vector<ll>; // Long long vector
    using llvec = std::vector<ull>; // Unsigned long long vector


    // The N value to evaluate
    
    const long long MOD {1000000007};


    // std::endl char, shortened.
    const char nl = '\n';



    /**
     * Populate vetor with ascending numbers.
     * Includes options `start` param.
    */
    template <typename NumType, typename VecNumType>
    void populator(NumType n, std::vector<VecNumType> &v, NumType start = 1) {
        for (NumType i = start; i <= n; i++) {
            v.push_back(i);
        }
    }



    /**
     * Append starting values to end of vector.
     * Allows for input of the number of values to "cycle" to the back of the vector.
    */
    template <typename VecNumType>
    void append_two(std::vector<VecNumType> &vec, int n_values=2) {
        Q tmp;
        for (int i = 0; i < n_values; i++) {
            tmp = vec[i];
            vec.push_back(tmp);
        }
    }



    // /**
    //  * Evalute chunks of vector elements
    // */
    // template <typename VecNumType>
    // long eval_three(std::vector<VecNumType> vec) {
    //     long idx=0;
    //     VecNumType *v_ptr = &vec;
    //     append_two(*v_ptr); // Add first two elements to end of vector.

    //     //int maxsize = *v_ptr.size()-2;


    //     for (int n = 0; n < *v_ptr.size(); n++) {

    //         if VMn(vec[n], vec[n+1], vec[n+2]) {

    //             idx = n+1;
    //             break;
    //         }
    //     }
    //     return idx;  
    // }


    template <typename VecNumType>
    bool VMn(const VecNumType& Val1, const VecNumType& Val2, const VecNumType& Val3) {
        if (Val1 < Val2) {
            if (Val2 < Val3) return true;
            else return false;
        } else {
            return false;
        }
    }
}

#endif
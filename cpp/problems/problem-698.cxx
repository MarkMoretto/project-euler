
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <iterator>
#include <sstream>

#include "problem-698.hxx"



// std::vector<char> split_int_string(std::string& string_input) {
//     std::vector<char> v_tmp;
//     for (const char &c : string_input) {
//         v_tmp.push_back(c);
//     }
//     return v_tmp;
// }


u_base_map string_frequency (std::string& string_input) {

    u_base_map temp_freq;
    
    for (const char &c : string_input) {
        std::unordered_map<char, int>::iterator itr = temp_freq.find(c);
        if (itr != temp_freq.end()) {
            itr -> second++;
        } else {
            std::pair<char, int> new_pair (c, 1);
            temp_freq.insert (new_pair);
        }
    }

    return temp_freq;
}

// void test_func(int &N) {
//     std::uint_fast64_t i = 0;
//     std::uint_fast64_t n;
//     std::uint_fast64_t incr = 1;
    
//     while (n < N) {
//         i += incr;
//         auto s = std::to_string(i);

//     }
// }

void print_info(std::vector<char>& vec);

int main() {
    // "123" value set.
    
    std::string target_set = "123";
    std::vector<char> ts_vec(target_set.begin(), target_set.end());
    u_base_set ts(target_set.begin(), target_set.end());

    u_base_map freq;

    std::string test1 = "1112213334";

    std::vector<char> key_vec;
    std::vector<char> val_vec;
    std::vector<char> k_diff;
    std::vector<char> v_diff;

    freq = string_frequency(test1);

    for (auto &e : freq) {
        key_vec.push_back(e.first);
        char tmp = e.second;
        val_vec.push_back(tmp);

    }

    // print_info(key_vec);

    std::sort(ts_vec.begin(), ts_vec.end());
    std::sort(key_vec.begin(), key_vec.end());
    std::sort(val_vec.begin(), val_vec.end());

    // Test data with 4 still validates, so check that
    bool vec_chk = false;
    vec_chk = std::includes(key_vec.begin(), key_vec.end(), ts_vec.begin(), ts_vec.end());

    if (vec_chk == 1) {
        std::cout << "All key chars in 123!" << std::endl;
        std::string val_str;
        for (auto &e : val_vec) {
            val_str += e;
        }
        vec_chk = std::includes(val_str.begin(), val_str.end(), target_set.begin(), target_set.end());
        if (vec_chk == 1) {
            std::cout << "All value chars in 123!" << std::endl;
        }

    }
    
    // // Set difference of key values and target values.
    // // If none, evaluate values.
    // std::set_difference(std::begin(key_vec), std::end(key_vec), std::begin(ts), std::end(ts), std::inserter(k_diff, std::begin(k_diff)));

    // if (k_diff.size() == 0) {
    //     std::set_difference(std::begin(val_vec), std::end(val_vec), std::begin(ts), std::end(ts), std::inserter(v_diff, std::begin(v_diff)));
    //     if (v_diff.size() == 0) {
    //         std::cout << "Test value " << &test1 << " is valid." << std::endl;
    //     }
    // }
        
    

    return 0;
}


void print_info(std::vector<char>& vec) {

    std::ostringstream oss (std::ostringstream::ate);
    int pos = 1;
    int vecsize = vec.size();

    oss << "Vector size: " << vecsize << std::endl;

    oss.str("\nKey vector values: \n");
    for (auto &k : vec) {
        if (pos < vecsize) {
            oss << k << ", " << std::endl;    
        } else {
            oss << k << std::endl;
        }
        pos += 1;
    }
    std::cout << oss.str() << std::endl;

}
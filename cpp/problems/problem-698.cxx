
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



int main() {
    // "123" value set.
    u_base_set ts;
    u_base_map freq;

    ts = {"1","2","3"};

    std::string test1 = "111221333";

    std::vector<char> v_key;
    std::vector<char> v_val;
    // std::vector<char>::iterator v_diff;

    freq = string_frequency(test1);

    for (auto &e : freq) {
        v_key.push_back(e.first);
        std::sort(v_key.begin(), v_key.end());

        char tmp = e.second;
        v_val.push_back(tmp);
        std::sort(v_val.begin(), v_val.end());
    }



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
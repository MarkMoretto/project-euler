
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <iterator>
#include <sstream>

#include "problem-698.hxx"


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


constexpr int max_res = 1000; // Reserve size for vectors
void print_info(std::vector<char>& vec);

int main(int argc, char* argv[]) {
    
    if (argc != 2) {
        std::cout << "Please pass numerical argument!";
        return 1;
    } 

    const char *N_char = argv[1];
    int N = std::stoi(N_char);


    // std::string test1 = "111221333"; // Should fail with value counts of 2, 3, 4
    // std::string test2 = "1221333"; // Should pass with value counts of 2, 2, 3
    // "123" value set.
    
    std::string target_set = "123";
    std::vector<char> ts_vec(target_set.begin(), target_set.end());
    std::set<char> ts_set(target_set.begin(), target_set.end());

    // u_base_map freq;

    u_base_map freq;

    int i = 0;
    int counter = 0;

    while (counter < N) {
        i += 1;

        std::string s = std::to_string(i);
        freq = string_frequency(s);

        std::vector<char> key_vec;
        std::vector<char> val_vec;
        std::vector<char> k_diff;
        std::vector<char> v_diff;

        for (auto &e : freq) {
            key_vec.push_back(e.first);
            char tmp = e.second;
            val_vec.push_back(tmp);
        }

        std::vector<char> res;
        res.reserve(max_res);

        std::sort(key_vec.begin(), key_vec.end());
        std::sort(ts_vec.begin(), ts_vec.end());
        std::vector<char>::iterator itr = std::set_difference(key_vec.begin(), key_vec.end(), ts_vec.begin(), ts_vec.end(), res.begin());
        
        res.resize(itr - res.begin()); 

        if (res.size() == 0) {

            std::string val_str;
            for (auto &e : val_vec) {
                val_str += std::to_string(e);
            }

            // std::cout << "Val_str: " << val_str << std::endl;
            std::set<char> val_str_set(val_str.begin(), val_str.end());
            std::vector<char> val_str_vec(val_str_set.begin(), val_str_set.end());

            std::vector<char> ress;
            ress.reserve(max_res);

            std::sort(val_str_vec.begin(), val_str_vec.end());
            std::vector<char>::iterator itrs = std::set_difference(val_str_vec.begin(), val_str_vec.end(), ts_vec.begin(), ts_vec.end(), ress.begin());
            ress.resize(itrs - ress.begin());

            if (ress.size() == 0) {
                // std::cout << "All value chars in 123!" << std::endl;
                counter += 1;
                // std::cout << "Counter value: " << counter << std::endl;
            }
            ress.shrink_to_fit();
        }

        res.shrink_to_fit();
        // std::cout << "i value: " << i << std::endl;
    }

    std::cout << "The 123 result for F(" << N << ") is: " << i << std::endl;
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
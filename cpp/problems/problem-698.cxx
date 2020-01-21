
#include <iostream>
#include <string>
#include <iterator>

#include "problem-698.hxx"




u_base_map string_frequency (std::string& string_input) {

    u_base_map temp_freq;
    int count = 0;
    
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


int main() {
    std::string test1 = "111221333";

    u_base_map freq;

    freq = string_frequency(test1);

    std::cout << "\nValue counts for string: " << test1 << std::endl;
    for (auto &e : freq) {
        std::cout << "{ " << e.first << " : " << e.second << " }" << std::endl;
    }

    return 0;
}


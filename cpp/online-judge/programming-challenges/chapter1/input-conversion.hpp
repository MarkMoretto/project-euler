/**
 * Input conversion
*/
#pragma once
#ifndef INPUTCONV_H_
#define INPUTCONV_H_


#include <vector>
#include <string>
#include <regex>
#include <sstream>


typedef std::string STRING;
typedef std::vector<int> IntVec;
typedef std::vector<std::string> StrVec;
typedef std::stringstream StringStream;


StrVec string_split(STRING s, STRING delim = " ") {
    StrVec tmps;
    
    auto start = 0U;
    auto end = s.find(delim);

    while (end != STRING::npos) {
        tmps.push_back(s.substr(start, end - start));
        start = end + delim.length();
        end = s.find(delim, start);
    }
    tmps.push_back(s.substr(start, end));
    return tmps;
}


IntVec string_to_int(STRING sinput) {
    IntVec outv;
    StringStream ss;
    // Convert to integer.

    StrVec sv = string_split(sinput);

    int ii;
    for (auto &c : sv) {
        ss << c;
        ss >> ii;
        outv.push_back(ii);
    }
    return outv;
}


void get_ints(STRING user_input) {

    STRING no_digits_pattern = "([\\D]+)";
    STRING ws_replacement = " ";

    // Init regex constructor
    std::regex ptrn (no_digits_pattern);

    std::cout << std::regex_replace(user_input, ptrn, ws_replacement);    
}


#endif
// g++ -Wall -Wextra -o palindrome so-palindrome-chk.cpp
#include <iostream>
#include <string>


using namespace std;

string nextSmallerPalindrome(string &s) {
    int n = s.length();
    string ans = "";
    
    if(n == 1) {
        s[0]--;
        return s;
    }
    
    if(s == "11") {
        return "9";
    }
    
   // For Handling odd cases
    if (n % 2 != 0) {
        int idx = n / 2;
        int diff = 0;

        if (s[idx] == '0') {
            s[idx] = '9';
            diff = 1;
        }
        else {
            s[idx]--;
        }
        
        idx--;
        
        while (idx >= 0 && diff == 1) {
            if (s[idx] == '0') {
                s[idx] = '9';
                idx--;

            } else {
                s[idx]--;
                diff = 0;
                break;
            }
        }
        
        int i = 0;
        while (i < n && s[i] == '0') {
            i++;
        }
        
        for(; i < n; i++) {
            // ans = ans + s[i];
            ans += s[i];
        }
        
        int new_n = ans.length();
        
        int j = 0;
        int k = new_n - 1;
        
        
        while(j < k) {
            if (ans[j] == ans[k]) {
                j++;
                k--;
            }
            else {
                ans[k] = ans[j];
                j++;
                k--;
            }
        }
        
        return ans;
    }
    // For handling even cases
    else {

        // int idx = n / 2 - 1;
        int idx = n / 2;
        int diff = 0;

        // cout << "Even case" << endl;
        // cout << "idx = " << idx << endl;

        if(s[idx] == '0') {
            s[idx] = '9';
            diff = 1;

        } else {
            s[idx]--;
        }

        idx--;

        while (idx >= 0 && diff == 1)
        {
            if (s[idx] == '0') {
                s[idx] = '9';
                idx--;
            }

            else {
                s[idx]--;
                diff = 0;
                break;
            }
        }
        
        int i = 0;
        // For ignoring Zeros from front of the string
        while (i < n && s[i] == '0') {
            i++;
        }
        
        //storing all the string s in new string ans after ignoring front 0
        for(; i < n; i++) {
            // ans = ans + s[i];
            ans += s[i];
        }
        
        int new_n = ans.length();
        
        int j = 0;
        int k = new_n - 1;
        
        // checking and changing the last half into first half
        while (j < k) {
            if (ans[j] == ans[k]) {
                j++;
                k--;

            } else {
                ans[k] = ans[j];
                j++;
                k--;
            }
        }
        return ans;
    }
}

int main() {
    std::string num;
    std::string *pNum = &num;
    std::cout << "Please enter a palindromic number: ";
    std::cin >> *pNum;
    // std::cout << "You have entered: " << num << std::endl;

    string res = nextSmallerPalindrome(*pNum);
    std::cout << "The next-largest palindrome is: " << res << std::endl;


    return 0;
}
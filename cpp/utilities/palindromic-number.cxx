/***********************************************************
Program to check whether an integer is a palindrome or not.

Contributor(s): Mark Moretto
Date: 2020-05-03
***********************************************************/

#include <iostream>

const char nl = '\n';


// template <typename T>
// std::optional <T> string_to() {
// }

// Reverse the input value.
void reverser(long n, long &out) {
    out = 0;
    long tmp;

    while (n != 0) {
        tmp = n % 10;
        out = (out * 10) + tmp;
        n /= 10;
    }
}

// Validate and return notification of success or failure.
void ispalindrome(long original, long result) {
    if (original == result) {
        std::cout << "Your number is a palindrome, Harry!";
    } else {
        std::cout << "Your number is NOT a palindrome.";
    }    
}

int main() {
    long res(0);
    long num;
    long * n_ptr = &num;

    std::cout << "Pleae enter a non-zero integer value" << nl << ">>>";
    std::cin >> num;

    reverser(*n_ptr, res);

    std::cout << "The reverse of " << num << " is " << res << nl;

    ispalindrome(*n_ptr, res);


    return 0;
}
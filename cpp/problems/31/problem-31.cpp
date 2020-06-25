/**
 * Topic: Project Euler
 * Problem 31
 * Title: Coin sums
 * URL: https://projecteuler.net/problem=31
*/


#include <iostream>
#include <vector>


// Array of coins to choose from (pence)
std::vector<int> coins{1, 2, 5, 10, 20, 50, 100, 200};

// Target value (GBP)
const int target_value = 200;


int main() {
    
    int max_n = target_value + 1;
    std::vector<int> combos(max_n, 0);
    combos.front();
    combos[0] = 1;

    for (int &c : coins) {
        for (int i = c; i <= target_value; ++i) {
            combos[i] += combos[i - c];
        }
    }

    std::cout << "The max combinations to make 200 pence is: " << combos.back() << std::endl;
    return 0;
}
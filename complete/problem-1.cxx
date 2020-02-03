// https://projecteuler.net/problem=1
#include <iostream>
#include <vector>
#include <numeric>

typedef std::vector<int> int_vec;
typedef int running_total;

bool ismultipleof(int &n, int divisor) {
    if (n % divisor == 0) {
        return true;
    } else {
        return false;
    }
}


int main() {
    size_t lim = 1000;
    int_vec testvec(lim);
    int i;
    std::iota(testvec.begin(), testvec.end(), 0);
    int running_total = 0;
    for (auto &ele : testvec) {
        if (ele > 0) {
            if (ismultipleof(ele, 3) || ismultipleof(ele, 5) || ismultipleof(ele, 15)) {
                running_total += ele;
                std::cout << "Multiple of 3 or 5: " << ele << std::endl;
            }            
        }
    }

    std::cout << "The sum of the run was: " << running_total << "\n";


    return 0;
}
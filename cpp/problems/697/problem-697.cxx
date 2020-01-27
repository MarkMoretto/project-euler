/*

https://www.learncpp.com/cpp-tutorial/73-passing-arguments-by-reference/

Notes:
    Need to compile with std=c++17 for template deducation.

TODO: Agg results and determine perecntage of n100 < 1.
*/

#include <iostream>
#include <random>
#include <chrono>
#include <cmath>
#include <functional>
// https://docs.microsoft.com/en-us/cpp/standard-library/random?view=vs-2019#code


int main() {
    // Credit for this random config actually working
    // https://stackoverflow.com/questions/9878965/rand-between-0-and-1

    std::mt19937_64 eng;
    std::uint64_t t_seed = std::chrono::high_resolution_clock::now().time_since_epoch().count();

    std::seed_seq ss{std::uint32_t(t_seed & 0xffffffff), std::uint32_t(t_seed >> 32)};
    eng.seed(ss);
    std::uniform_real_distribution<double> urd(0, 1);


    double c = 1.8e40;
    double* c_ptr = &c;
    // std::cout << "Log10 of c: " << std::log10(c) << std::endl;
    const double threshold = 1.0; // Value c should dip below to terminate loop
    const int N_TRIALS = 1000000;
    int lt1_count = 0;
    

    double current;
    double previous;
    double randn;
    // int n;
    int i;

    // Run a trial and record 0 or 1 if n < 100.
    for (i = 0; i < N_TRIALS; ++i) {
        current = *c_ptr;
        int n = 0;
        while (true) {
            if (current < threshold) {
                break;
            }

            randn = urd(eng);
            previous = current;       
            current = previous * randn;
            n++;
        }
        // std::cout << "Number of iterations for c to go below 1: " << n << std::endl;
        if (n == 100) {
            lt1_count += 1;
        }
    }

    std::cout << "Number of successful trials: " << lt1_count << std::endl;

    return 0;
}


void incr_c(double& c_value) {
    c_value += 1;
}

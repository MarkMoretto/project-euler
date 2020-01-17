/*


Notes:
    Need to compile with std=c++17 for template deducation.

TODO: Agg results and determine perecntage of n100 < 1.
*/


#include <random>
#include <iostream>
#include <ostream>


// Declare functions
int run_sim(double& initial_c);

std::random_device rd;
std::mt19937_64 eng(rd());
std::uniform_real_distribution urd(0.0, 1.0);

int main() {
    // int n_iters = 10;
    // int i;

    double c = 1.8e30;
    // int n_trials = 100;
    // std::cout << "Initial c value: " << c << std::endl;

    int result = run_sim(c);
    std::cout << "Number of iterations for c to go below 1: " << result << std::endl;

    return 0;
}

int run_sim(double& initial_c) {

    // n0 -> current = initial_c
    // Having `previous` is just to be explicity about the operation.
    double current = initial_c;
    double previous;
    int n = 0;
 
    while (true) {
        // Summary: Increment n by 1 until current drops below 1.
        if (current < 1.0) {
            break;
        }
        previous = current;
        current = previous * urd(eng);
        n = n + 1;
    }

    return n;
}

// May want to consider incrementing large values via string method.
// https://stackoverflow.com/questions/19556340/incrementing-big-numbers-nearly-100-000-digits-in-c
// or: https://gmplib.org/

void increment_value() {


}
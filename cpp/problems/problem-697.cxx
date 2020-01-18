/*

https://www.learncpp.com/cpp-tutorial/73-passing-arguments-by-reference/

Notes:
    Need to compile with std=c++17 for template deducation.

TODO: Agg results and determine perecntage of n100 < 1.
*/

#include <iostream>
#include <cstdlib>
#include <random>
#include <ctime>
#include <errno.h>
#include <math.h>


// using base_engine = std::default_random_engine;
// using urd = std::uniform_real_distribution<double>;
// base_engine dre {};
// urd zero_to_one {0, 1};
// auto randn = std::bind(zero_to_one, dre);


// Declare functions
double rand_zero_to_one();
double rand_x_to_y(double min, double max);
int run_sim(double& initial_c);


int main() {
    std::random_device rd{};
    // srand (static_cast <unsigned> (time(0)));
    srand(rd());

    // int n_iters = 10;
    // int i;

    double c = 1.8e40;
    // int n_trials = 100;
    // std::cout << "Initial c value: " << c << std::endl;
    // for (int i=0; i<10; ++i) {
    //     std::cout << urd(0, 1) << std::endl;
    // }
    int result = run_sim(c);
    std::cout << "Number of iterations for c to go below 1: " << result << std::endl;

    return 0;
}

double rand_zero_to_one() {
    return std::rand() / (RAND_MAX + 1.);
}

double rand_x_to_y(double min, double max) {
    static int first = -1;
    if ((first = (first < 0))) {
        srand (static_cast <unsigned> (time(0)));
    }

    if (min >= max) {
        return errno = EDOM, NAN;
    }

     return min + (rand() / ( RAND_MAX / (max - min) ) ) ;  
}




int run_sim(double& initial_c) {
    // std::uniform_real_distribution<double> dist(0, 1);
    // n0 -> current = initial_c
    // Having `previous` is just to be explicity about the operation.
    double current = initial_c;
    // double previous;
    int n = 0;

    double randn;
    // double curr_rand, prev_rand;
    // randn = rand_zero_to_one();
 
    while (true) {
        // curr_rand = rand_zero_to_one();
        // Summary: Increment n by 1 until current drops below 1.
        if (current < 1.0) {
            break;
        }

        // randn = rand_x_to_y(0., 1.);
        // prev_rand = rand_zero_to_one();
        // randn = eval_rand(curr_rand, prev_rand);
        randn = rand_x_to_y(0, 1);

        // previous = current;
        // current = previous * randn;
        current *= randn;
        n = n + 1;
    }

    return n;
}


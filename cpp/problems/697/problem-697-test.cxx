
#include <iostream>
#include <random>
#include <chrono>


// Declare functions
// int run_sim(double& initial_c);


int main() {
    // int n_iters = 10;
    // int i;

    /**** Working random setup for while loop. Requires <chrono>
    std::mt19937_64 eng;
    std::uint64_t t_seed = std::chrono::high_resolution_clock::now().time_since_epoch().count();
    // std::cout << "Value of t_seed: " << t_seed << std::endl;
    std::seed_seq ss{std::uint32_t(t_seed & 0xffffffff), std::uint32_t(t_seed >> 32)};
    eng.seed(ss);
    std::uniform_real_distribution<double> urd(0, 1);
    */

    /*** Working demo **/
    /*
    int i = 0;
    const int MAX_ITER = 10;
    double randn;
    while (i < MAX_ITER) {
        ++i;
        randn = urd(eng);
        
        std::cout << "Random number: " << randn << std::endl;
    }
    */


    double c = 1.8e10;
    double incr = 1;
    int n_trials = 100;
    // std::cout << "Initial c value: " << c << std::endl;
    std::cout << "Starting value of c: " << c << std::endl;
    for (int i = 0; i < 2000000; ++i) {
        c = c + incr;
    }
    std::cout << "Ending value of c: " << c << std::endl;
    // int result = run_sim(c);
    // std::cout << "Number of iterations for c to go below 1: " << result << std::endl;

    return 0;
}


// void run_sim(double& initial_c, int& nOut) {

//     std::uniform_real_distribution<double> unf(0, 1);
//     // n0 -> current = initial_c
//     // Having `previous` is just to be explicity about the operation.
//     double current = initial_c;
//     double previous;
//     // int n = 0;

//     // double randn;
//     // double curr_rand, prev_rand;
//     // randn = rand_zero_to_one();
 
//     while (true) {
//         double randn = randomize(unf);
//         std::cout << randn << std::endl;
//         // Summary: Increment n by 1 until current drops below 1.
//         if (current < 1.0) {
//             break;
//         }


//         previous = current;
//         current = previous * randn;
//         // current *= randn;
//         nOut++;
//     }

//     // return n;
// }


// int run_sim(double& initial_c) {
//     // 

//     std::random_device rd;
//     std::mt19937_64 eng(rd());
//     std::uniform_real_distribution urd(0.0, 1.0);

//     // n0 -> current = initial_c
//     // Having `previous` is just to be explicity about the operation.
//     double current = initial_c;
//     double previous;
//     int n = 0;
 
//     while (true) {
//         // Summary: Increment n by 1 until current drops below 1.
//         if (current < 1.0) {
//             break;
//         }
//         previous = current;
//         current = previous * urd(eng);
//         n = n + 1;
//     }

//     return n;
// }

// May want to consider incrementing large values via string method.
// https://stackoverflow.com/questions/19556340/incrementing-big-numbers-nearly-100-000-digits-in-c
// or: https://gmplib.org/

// void increment_value() {}


// May want to consider incrementing large values via string method.
// https://stackoverflow.com/questions/19556340/incrementing-big-numbers-nearly-100-000-digits-in-c
// or: https://gmplib.org/

// void find_c() {
//     double incr = 1;
//     int n_trials = 100;
//     // std::cout << "Initial c value: " << c << std::endl;
//     std::cout << "Starting value of c: " << c << std::endl;
//     for (int i = 0; i < 2000000; ++i) {
//         c = c + incr;
//     }

// }


// // https://stackoverflow.com/questions/686353/random-float-number-generation
// std::default_random_engine& randf() {
//     static std::default_random_engine u{};
//     return u;
// }

// void randomize() {
//     static std::random_device rd{};
//     // auto eng = randf();
//     // eng.seed(rd());
//     randf().seed(rd());
//     // double random_n = dist(eng);
// }

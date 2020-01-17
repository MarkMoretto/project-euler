// https://doc.rust-lang.org/stable/rust-by-example/mod.html
extern crate rand;

// use rand::prelude::*;
use rand::{thread_rng, Rng};

// https://doc.rust-lang.org/rust-by-example/fn/methods.html
struct Trials {
    done: bool,
    randn: f64,
    c: f64,
    curr: f64,
    n_iterations: u64,
}

impl Trials {
    fn n_incr_1(&mut self) {
        self.n_iterations += 1;
    }

    fn sim(&mut self) -> u64 {
        let mut rng = thread_rng();

        let mut done: bool = false;

        // Current value of "c".
        let mut curr: f64 = init_c;

        let mut n: u64 = 1;

        while !self.done {
            // Check curr early.  If c = 1.0 to start, then
            // Stop loop if it does.
            if self.curr < 1.0 {
                self.done = true;
            }

            // Skip over the initial n value  of zero
            // set current to the value of c at the start.
            self.randn = rng.gen();

            // Multiply current value by random number between 0 and 1.
            self.curr *= self.randn;

            // Increment n here; If c * randn < 1.0 to start, then this should
            // self.n_iterations += 1;
            self.n_incr_1();
        }
        return self.n_iterations;
    }
}

fn main() {
    // let mut rng = thread_rng();
    // let mut randn: f64;

    // let range_len: u32 = 100;
    // let mut n: u32 = 0;
    // let arange: Vec<u32> = (0..range_len).collect();
    // let mut results = Vec::<f64>::with_capacity(100);

    let c: f64 = 1e10;
    // let mut curr: f64 = c;
    // let mut done: bool = false;
    // let mut n = 1;

    let result: u64 = sim(c);

    println!("Number of iterations: {}", result);
}

// fn sim(init_c: f64) -> u64 {
//     let mut rng = thread_rng();
//     let mut randn: f64;

//     let mut done: bool = false;

//     // Current value of "c".
//     let mut curr: f64 = init_c;

//     let mut n: u64 = 1;

//     while !done {
//         // Check curr early.  If c = 1.0 to start, then
//         // Stop loop if it does.
//         if curr < 1.0 {
//             done = true;
//         }

//         // Skip over the initial n value  of zero
//         // set current to the value of c at the start.
//         randn = rng.gen();

//         // Multiply current value by random number between 0 and 1.
//         curr *= randn;

//         // Increment n here; If c * randn < 1.0 to start, then this should
//         n += 1;
//     }
//     return n;
// }

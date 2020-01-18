// https://doc.rust-lang.org/stable/rust-by-example/mod.html
extern crate rand;

// use rand::prelude::*;
use rand::Rng;

// // https://doc.rust-lang.org/rust-by-example/fn/methods.html
// struct Trials {
//     c: f64,
// }

// // Notes: Not currently working.
// impl Trials {
//     fn sim(self) -> u64 {
//         let mut rng = thread_rng();
//         let mut randn: f64;
//         let mut done: bool = true;
//         let mut n: u64 = 0;
//         let mut curr: f64 = self.c;

//         while !done {
//             // Check curr early.  If c = 1.0 to start, then
//             // Stop loop if it does.
//             if curr < 1.0 {
//                 done = true;
//             }

//             // Skip over the initial n value  of zero
//             // set current to the value of c at the start.
//             randn = rng.gen();

//             // Multiply current value by random number between 0 and 1.
//             curr *= randn;

//             // Increment n here; If c * randn < 1.0 to start, then this should
//             n += 1;
//         }
//         return n;
//     }
// }


fn main() {
    let mut rng = rand::thread_rng();
    let mut randn: f64;
    let n_trials = 100;

    // Could also create a quick range of random numbers to iterate
    // let rand_vec: Vec<f64> = (0..100).map(|_| { rng.gen_range(0.0_f64, 1.0_f64) }).collect();
    // println!("{:?}", rand_vec[2]);

    let mut c: f64 = 1e40;
    let mut c_ref: f64;
    let mut n: i64;
    let mut current: f64;
    let mut done: bool = false;
    let mut epoch_count: i64 = 0;
    let mut max_goal = 0_i64;

    // let mut results = Vec::<f64>::with_capacity(100);


    let mut goal: i64 = 0;

    while !done {

        // goal = 0; // Want goal to get to 24 positive results.
        // println!("Goal reset.");
        epoch_count += 1;

        for _ in 0..n_trials {

            n = 0;
            current = c;

            while current >= 1.0_f64 {
                randn = rng.gen();
                current *= randn;
                n += 1;
            }

            if n == 100 {
                goal += 1;
            }
        }


        if goal < 24 {
            if goal > max_goal {
                max_goal = goal;
                println!("New goal count high: {:?}", goal);
                println!("Curent c value: {:E}", c);
            }
            
            if epoch_count as f64 % 100.0 == 0.0 {
                println!("Curent c value: {:?}", c);
            }

            c += 1e7;
            goal = 0;

        } else {
            done = true;
        }


    }

    
    println!("Targets met: {:?}", goal);
    println!("Epoch count: {:?}", epoch_count);
    println!("Final c value: {:?}", c);
    println!("Final c log10 value: {:.5}", c.log10());

    
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

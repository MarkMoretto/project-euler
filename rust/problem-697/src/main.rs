// https://doc.rust-lang.org/stable/rust-by-example/mod.html
extern crate rand;

// use rand::prelude::*;
use rand::Rng;



fn main() {
    let mut rng = rand::thread_rng();
    
    let n_trials: i64 = 100; // Number of n trials to run for each test.

    // Starting c value
    let mut c: f64 = 1e45;

    // Target ercentage (out of 100) as threshold.
    let target_pct: i64 = 25;

    // Various counts
    let mut epoch_count: i64 = 0;
    let mut goal: i64 = 0; // Counter of goals reached
    let mut max_goal: i64 = 0;

    // Increment values
    let incr_int: i64 = 1;

    // Final done indicator
    let mut all_done: bool = false;

    while !all_done {

        // while goal < target_pct {}

        epoch_count += incr_int;

        for _ in 0..n_trials {

            let mut n: i64 = 0;
            let mut current = c;

            while current >= 1.0 {
                let randn: f64 = rng.gen();
                current *= randn;
                n += incr_int;
            }

            if n == 100 {
                goal += incr_int;
            }
        }


        if goal < target_pct {
            if goal > max_goal {
                max_goal = goal;
                println!("\n{0}{1:<2}{x}", "Targets met", ":", x=goal);
                println!("\t{0}{1:<2}{x}", "Epoch count", ":", x=epoch_count);
                println!("\t{0}{1:<2}{x:.5E}", "Current C value", ":", x=c);
                println!("\t{0}{1:<2}{x:.10E}", "Current log10 C value", ":", x=c.log10());

            }
            
            c += 1e40;
            goal = 0;

        } else {
            all_done = true;
        }

    }

    println!("\n\nFinal Results:");
    println!("\t{0}{1:<2}{2}", "Targets met", ":", goal);
    println!("\t{0}{1:<2}{2}", "Epoch count", ":", epoch_count);
    println!("\t{0}{1:<2}{2:.5E}", "C value", ":", c);
    println!("\t{0}{1:<2}{2:.10E}", "C log10 value", ":", c.log10());
    
}

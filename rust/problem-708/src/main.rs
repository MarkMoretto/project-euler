// use std::collections::{HashMap, HashSet};
// use std::env;

// static INCR: u64 = 1;


pub fn pfs(n: &mut u64) -> Vec<u64> {
    // prime factors
    // https://github.com/sporto/exercism/tree/master/rust/prime-factors

    let mut x_vec: Vec<u64>;
    x_vec = Vec::with_capacity(*n as usize);

    let mut div = 2;

    while *n > 1 {
        while *n % div == 0 {
            x_vec.push(div);
            *n = *n / div;
        }
        div += 1;
    }
    x_vec
}

fn print_results(x: u64, y: Vec<u64>) {
    println!("The prime factors of {} are: {:?}", x, y);
}

fn main() {
    // Reference mutability: https://stackoverflow.com/questions/40921712/rust-mutable-value-vs-mutable-reference
    let mut test_pfs = 60_u64;
    let q = &mut test_pfs;
    let v_pfs: Vec<u64> = pfs(q);
    print_results(test_pfs, v_pfs);
}

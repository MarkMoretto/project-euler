fn primes(limit: &u64) -> Vec<u64> {
    let mut x_vec: Vec<_> = (2..*limit).collect();
    for p in 2..*limit {
        x_vec.retain(|&x| x <= p || x % p != 0);
    }
    x_vec
}

fn main() {
    let tst1: u64 = 6;
    let res: Vec<u64> = primes(&tst1);
    println!("The first {:?} prime numbers are: {:?}", tst1, res);
}

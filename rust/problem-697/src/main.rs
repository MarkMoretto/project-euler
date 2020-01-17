extern crate rand;

use rand::Rng;

fn main() {
    let mut rng = rand::thread_rng();
    let n1: u8 = rng.gen();
}
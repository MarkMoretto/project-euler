extern crate rand;

use rand::Rng;
use rand::distributions::Uniform;

struct RandSampler {
    rand_u8: u8,
    rand_u16: u16,
}

fn main() {
    let mut rng = rand::thread_rng();
    let randers = RandSampler { rand_u8: rng.gen(), rand_u16: rng.gen() };
    
    println!("Random u8: {}", &randers.rand_u8);
    println!("Random u16: {}", &randers.rand_u16);

}



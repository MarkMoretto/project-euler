



fn main() {
    let k: usize = 20;
    let a = 2;
    let b = 5;

    let mut vec = Vec::with_capacity(k);
    
    vec.extend([a, b].iter().cloned());
    assert_eq!(vec.capacity(), 20);
    vec.shrink_to_fit();
    
    println!("The values of a and b are: ({}, {})", vec[0], vec[1]);
}

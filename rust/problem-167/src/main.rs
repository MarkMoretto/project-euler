



fn main() {
    let k: usize = 20;
    let a = 2_u32;
    let b = 5_u32;

    let mut vec: Vec<u32> = Vec::with_capacity(k);

    vec.extend([a, b].iter().cloned());
    assert_eq!(vec.capacity(), 20);
    vec.shrink_to_fit();
    
    println!("The values of a and b are: ({}, {})", vec[0], vec[1]);

    let xx = 3_i32;
    println!("The value of 3i32 is {}", xx);
}

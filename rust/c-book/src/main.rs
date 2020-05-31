
mod utils;
use utils::chapters::ch1;


fn main() {
    let fahr: u32 = 60; // Input Fahrenheit temperature
    let res = ch1::f_to_c(fahr);
    println!("Temp {}F is {:.2}C", fahr, res);
}

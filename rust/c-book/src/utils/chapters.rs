// C Programming Language - Chapter 1 exercises


// Suppress all warnings from casts which overflow.
#![allow(overflowing_literals)]


pub mod ch1 {
    // Return calculation of Celsius
    pub fn f_to_c(f: u32) -> f32 {
        return (5_f32 * (f as f32 - 32_f32)) / 9_f32;
    }

}
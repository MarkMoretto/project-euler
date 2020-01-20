
use std::str;


use std::collections::HashSet;
//#[derive(Hash, Eq, PartialEq, Debug)]

// #[derive(Debug)]
struct Known<'a> {
    value: &'a str,
}


//https://users.rust-lang.org/t/solved-how-to-split-string-into-multiple-sub-strings-with-given-length/10542/7
fn sub_strings(string: &str, sub_len: usize) -> Vec<&str> {
    let mut subs = Vec::with_capacity(string.len() / sub_len);
    let mut iter = string.chars();
    let mut pos = 0;

    while pos < string.len() {
        let mut len = 0;
        for ch in iter.by_ref().take(sub_len) {
            len += ch.len_utf8();
        }
        subs.push(&string[pos..pos + len]);
        pos += len;
    }
    subs
}



fn main() {

    // Closure
    // Like a lambda. The curly brackets and types are optional
    let incr = | i : u64 | -> u64 { i + 1_u64 };

    let _f4 = Known { value: "11" };
    let _f10 = Known { value: "31" };
    let _f40 = Known { value: "1112" };
    let _f1000 = Known { value: "1223321" };
    let _f6000 = Known { value: "2333333333323" };

    assert_eq!(_f4.value, "11");

    println!("f4 value: {k_value}", k_value = _f4.value);

    let trgt_set: HashSet<&str> = vec!["1", "2", "3"].into_iter().collect();


    // Split a string by each character
    let split_size: usize = 1;
    println!("{:?}", sub_strings(f6000.value, split_size));

    // Letter frequency
    // https://www.rosettacode.org/wiki/Letter_frequency#Rust
}

use std::str;
use std::fs;

use std::collections::{HashSet, HashMap};
//#[derive(Hash, Eq, PartialEq, Debug)]

// #[derive(Debug)]
struct Known<'a> {
    value: &'a str,
}


//https://users.rust-lang.org/t/solved-how-to-split-string-into-multiple-sub-strings-with-given-length/10542/7
fn split_str_by_len(string_input: &str, char_len: usize) -> Vec<&str> {
    let mut output = Vec::with_capacity(string_input.len() / char_len);
    let mut iter = string_input.chars();
    let mut pos = 0;
    
    while pos < string_input.len() {
        let mut len = 0;
        for x in iter.by_ref().take(char_len) {
            len += x.len_utf8();
        }
        output.push(&string_input[pos..pos + len]);
        pos += len;
    }
    output
}


fn main() {

    // Closure
    // Like a lambda. The curly brackets and types are optional
    let incr = | i : u64 | -> u64 { i + 1_u64 };

    let trgt_set: HashSet<&str> = vec!["1", "2", "3"].into_iter().collect();

    let f6000 = Known { value: "2333333333323" };

    // // Split a string by each character
    // let split_size: usize = 1;
    // //println!("{:?}", split_str_by_len(f6000.value, split_size));

    // // Letter frequency
    // // https://www.rosettacode.org/wiki/Letter_frequency#Rust
    // let mut freq_count = HashMap::new();
    // let mut split_vec = split_str_by_len(f6000.value, split_size);

    // for c in f6000.value.chars() {
    //     *freq_count.entry(c).or_insert(0) += 1;
    // }

    // println!("Number of occurrences per character:\n");
    // for (ch, &count) in &freq_count {
    //     println!("{0:?}: {1}", ch, count);
    // }

    let _dir = String::from("S:\\OFP\\Hedis\\Population Health File Downloads\\HAP");
    let _files = fs::read_dir(_dir).unwrap();

    for f in _files {
        println!("{}", f.unwrap().path().display());
    }
}

// #[allow(dead_code)]
// fn test1() {

//     let f4 = Known { value: "11" };
//     let f10 = Known { value: "31" };
//     let f40 = Known { value: "1112" };
//     let f1000 = Known { value: "1223321" };
//     let f6000 = Known { value: "2333333333323" };

//     assert_eq!(f4.value, "11");
//     println!("f4 value: {k_value}", k_value = f4.value);

// }
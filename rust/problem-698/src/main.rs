use std::collections::{HashMap, HashSet};
use std::env;

//#[derive(Hash, Eq, PartialEq, Debug)]
static INCR: u64 = 1;

fn main() {
    let arg_vec: Vec<String> = env::args().collect();

    if arg_vec.len() < 2 {
        panic!("Command line argument missing!");
    } else {
        let trgt_values = "123";
        let trgt_set: HashSet<char> = trgt_values.chars().collect();

        // Letter frequency dictionary
        let mut freq_count: HashMap<char, u64> = HashMap::new();

        let input_n: String = arg_vec[1].to_string();

        let target_n: u64 = input_n.parse::<u64>().unwrap();
        println!("Your input value is: {:?}", target_n);

        let mut n: u64 = 0;
        let mut count: u64 = 0;

        while count < target_n {
            n += INCR;
            let mut inner_count: u64 = 0;
            let s: String = n.to_string();
            // println!("Current n and s: {0:?}\t{1:?}", n, s);

            // Check to see if all of hte current chracters are in the target set
            if s.chars().all(|c| trgt_set.contains(&c)) {
                // println!("At s.chars() check part.");
                for ch in s.chars() {
                    *freq_count.entry(ch).or_insert(0) += 1;
                }

                // Dictionary values converted to string type and collected into a set.
                let dict_vals: HashSet<String> =
                    freq_count.values().map(|x| x.to_string()).clone().collect();
                // println!("Past dict_vals part");

                // Check if all frequency values in target set
                // If so, increment the counter by 1
                let merged: String = dict_vals.iter().map(|x| x.chars()).flatten().collect();
                // println!("Merged value: {:#?}", merged);
                if merged.chars().all(|c| trgt_set.contains(&c)) {
                    // count += INCR;
                    inner_count += INCR;
                }
            }
            count += inner_count;
            // println!("Current count: {:?}", count);
        }

        println!("Result for F({0:?}): {1:?}", &target_n, n);
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

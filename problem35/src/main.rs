extern crate time;

use std::time::SystemTime;

fn main() {
    let now = SystemTime::now();
    let mut array: [bool; 1000000] = [true;1000000];
    array[0] = false;
    array[1] = false;
    for x in 2..1000 {
        if array[x] {
            let mut temp: u64 = x as u64;
            temp = temp * (x as u64);
            let add: u64 = x as u64;
            while temp < 1000000 {
                array[temp as usize] = false;
                temp = temp + add;
            }
        }
    }
    let mut total = 0;
    for x in 0..1000000 {
        if array[x] {
            //println!("Prime: {}", x);
            let num = String::from(format!("{}",x));
            let len = num.len();
            let mut valid: bool = true;
            for y in 1..len {
                let front: String = format!("{}",&num[y..num.len()]);
                let back: String = format!("{}",&num[0..y]);
                let i: usize = format!("{}{}",front,back).parse().unwrap();
                let is_prime: bool = array[i];
                if !is_prime {
                    valid = false;
                    break;
                }
            }
            if valid {
                total = total + 1;
            }
        }
    }
    println!("Total: {}",total);
    match now.elapsed() {
        Ok(elapsed) => {
            let nanos = elapsed.subsec_nanos() as u64;
            println!("Time Taken: {}ms", (1000*1000*1000* elapsed.as_secs() + nanos)/(1000*1000));
        }
        Err(e) => {
            println!("Error: {:?}", e);
        }
    }
}

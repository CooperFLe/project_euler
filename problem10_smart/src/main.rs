extern crate time;

use std::time::SystemTime;

fn main() {
    let now = SystemTime::now();
    let mut array: [bool; 2000000] = [true;2000000];
    array[0] = false;
    array[1] = false;
    for x in 2..1414 {
        if array[x] {
            let mut temp: u64 = x as u64;
            temp = temp * (x as u64);
            let add: u64 = x as u64;
            while temp < 2000000 {
                array[temp as usize] = false;
                temp = temp + add;
            }
        }
    }

    let mut sum: u64 = 0;

    for x in 0..2000000 {
        if array[x] {
            sum = sum + (x as u64);
            //println!("Prime: {}", x);
        }
    }

    println!("Sum: {}", sum);

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

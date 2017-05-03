extern crate time;

use std::time::SystemTime;

fn main() {
    let now = SystemTime::now();
    let mut sum: u64 = 0;
    for x in 3..2000000 {
        let mut prime = true;
        let mut y = 2;
        while prime && y < x-1 {
            if x%y==0 {
                prime = false;
            }
            y = y + 1;
        }
        if prime {
            sum = sum + x;
        }
    }

    println!("Sum of primes: {}", sum+2);

    match now.elapsed() {
        Ok(elapsed) => {
            let time = elapsed.as_secs();
            let min = time/60;
            let sec = time%60;
            println!("Time Taken: {}min {}sec", min, sec);
        }
        Err(e) => {
            println!("Error: {:?}", e);
        }
    }
}

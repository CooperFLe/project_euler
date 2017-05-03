extern crate time;

use std::time::SystemTime;

fn main() {
    let now = SystemTime::now();

    let mut array1: [u8; 1000] = [0;1000];
    let mut array2: [u8; 1000] = [0;1000];
    array1[0] = 1;
    array2[0] = 1;
    fn add(arr1: [u8; 1000], arr2: [u8;1000]) -> [u8;1000]{
    let mut arr: [u8;1000] = [0;1000];
    let mut carry: bool = false;
        for x in 0..1000 {
            let sum: u8 = arr1[x] + arr2[x];
            arr[x] = sum%10;
            if carry {
                if arr[x] == 9 {
                    arr[x] = 0;
                    carry = true;
                }
                else {
                    arr[x] = arr[x] + 1;
                    carry = false;
                }
            }
            if sum > 9 {
                carry = true;
            }
        }
        arr
    }

    let mut index = 3;
    while array1[999] < 1 {
        let array3: [u8; 1000] = add(array1, array2);
        array1 = array2;
        array2 = array3;
        index = index + 1;
    }

    println!("Index: {}", index-2);

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

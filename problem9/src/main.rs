fn main() {
    for x in 1..1000/2 {
        for y in 1..1000/2 {
            let z: u32 = 1000 - x - y;
            if (x*x) + (y*y) == (z*z) {
                println!("A: {} B: {} C: {}",x,y,z);
                println!("Product: {}", (x*y*z));
                return;
            }
        }
    }
}

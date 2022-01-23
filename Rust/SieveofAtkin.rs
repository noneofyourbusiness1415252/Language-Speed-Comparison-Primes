fn main() {
	let limit = std::env::args().collect::<Vec<String>>()[1].parse::<u32>().unwrap();
	let mut sieve = vec![false; (limit + 1) as usize];
	let sqrt = ((limit as f32).sqrt()) as u32;
	for i in 1..=sqrt {
		let isquare = i * i;
		let triple_isquare = isquare * 3;
		for j in 1..=sqrt {
			let jsquare = j * j;
			let mut n = 4 * isquare + jsquare;
			if n <= limit && [1, 5].contains(&(n % 12)) {
				sieve[n as usize] = !sieve[n as usize]
			}
			n = triple_isquare + jsquare;
			if n <= limit && n % 12 == 7 {
				sieve[n as usize] = !sieve[n as usize]
			}
			n = triple_isquare - jsquare;
			if i > j && n <= limit && n % 12 == 11 {
				sieve[n as usize] = !sieve[n as usize]
			}
		}
	}
	for i in 5..sqrt {
		if sieve[i as usize] {
			let isquare = i * i;
			for j in (isquare..=limit).step_by(isquare as usize) {
				sieve[j as usize] = false
			}
		}
	}
	print!("2, 3");
	let mut total = 2u32;
	for p in (5..limit).filter(|x| sieve[*x as usize]) {
		print!(", {}", p);
		total += 1
	}
	println!("\nTotal: {}", total)
}

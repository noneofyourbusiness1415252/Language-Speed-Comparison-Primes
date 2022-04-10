use std::{*, process::*};
fn input<T: str::FromStr>(prompt: &str) -> T
where
	T::Err: fmt::Display,
{
	println!("{}\x1b[96m", prompt);
	let mut tmp = String::new();
	loop {
		io::stdin().read_line(&mut tmp).unwrap();
		print!("\x1b[0m");
		match tmp.trim().parse::<T>() {
			Ok(res) => break res,
			Err(err) => {
				eprintln!("\x1b[91m{}\nTry again!\x1b[96m", err)
			}
		}
		tmp.clear();
	}
}
fn main() {
	let mut langs = [
		"C", "C++", "Rust", "Go", "C♯", "Java", "Kotlin", "VB", "Swift", "PHP",
		"Node.js", "Dart", "Python", "R",
	];
	let mut limit: u32 = input("Enter a number for the first test");
	let pattern: u32 = input(
		"Enter a number to multiply the amount of numbers tested on each time",
	);
	loop {
		println!("Times with \x1b[96m{}\x1b[0m numbers:", limit);
		let mut times = collections::HashMap::new();
		for i in &langs {
			let args;
			let mut command = Command::new(match *i {
				"Python" | "Java" | "Ruby" | "PHP" => {
					args = i.to_lowercase();
					&args
				}
				"Node.js" => "node",
				"R" => "Rscript",
				_ => {
					args = format!("{}/primes", i);
					&args
				}
			});
			match *i {
				"Java" => command.args(["-cp", "Java", "primes"]),
				"Python" => command.arg("primes.py"),
				"Node.js" => command.arg("primes.js"),
				"PHP" => command.arg("primes.php"),
				"Ruby" => command.arg("primes.rb"),
				"R" => command.arg("primes.r"),
				_ => &command,
			};
			print!("\x1b[96m{}\x1b[0m: ", i);
			command
				.arg(format!("{}", limit))
				.stdout(Stdio::null())
				.stderr(Stdio::null());
			let (start, status) = (time::Instant::now(), command.status().unwrap());
			if status.success() {
				times.insert(*i, start.elapsed().as_secs_f32());
				println!("\x1b[96m{0:.3}\x1b[0m", times.get(i).unwrap())
			} else {
				eprintln!("\x1b[91m{}\x1b[0m", status);
			}
		}
		limit *= pattern;
		langs.sort_by(|a, b| times.get(a).partial_cmp(&times.get(b)).unwrap());
		println!(
			"Multipliers, relative to \x1b[38;2;0;255;0m{}\x1b[0m:",
			langs[0]
		);
		let fastest = times.get(langs[0]).unwrap();
		for i in &langs[1..] {
			let multiplier = times.get(i).unwrap() / fastest;
			let green = (256. / multiplier) as u8;
			println!(
				"\x1b[38;2;{};{};0m{}: {3:.1}\x1b[0m",
				255 - green,
				green,
				i,
				multiplier,
			);
		}
	}
}

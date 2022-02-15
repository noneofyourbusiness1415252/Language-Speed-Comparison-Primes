from timeit import timeit
from os import environ
reset, diamond, red, langs = (
	"\033[0m",
	"\033[1;38;2;185;242;255m",
	"\033[31m",
	["C", "C++", "Rust", "Go", "C#", "Kotlin", "NodeJS", "Java", "Python", "Ruby"],
)
print("Enter a number for the first test", diamond)
while True:
	try:
		limit = int(eval(input()))
	except:
		print("\033[31mError: Please enter an integer", diamond)
	else:
		break
print(
	f"{reset}Enter a pattern to increase the numbers tested each time, e.g. +5 (add 5"
	" each time), *4 (multiply by 4 each time), **2 (square each time)",
	diamond,
)
while True:
	try:
		pattern = input()
		eval(f"{limit} {pattern}")
	except:
		print(f"{red}Error: Please enter a valid pattern: ", end=diamond)
	else:
		break
while True:
	print(f"{reset}Times with {diamond}{limit}{reset} numbers:")
	times = {}
	for i in langs:
		match i:
			case "Python":
				args = "'python', 'primes.py'"
			case "Java":
				args = f"'java', '-cp', 'Java', 'primes'"
			case "NodeJS":
				args = "'node', 'primes.js'"
			case "Ruby":
				args = "'ruby', 'primes.rb'"
			case _:
				args = f"'./{i}/primes'"
		try:
			times[i] = timeit(
				f"run([{args}, '{limit}'], stdout=DEVNULL, stderr=DEVNULL, check=True)",
				"from subprocess import run, DEVNULL",
				number=1,
			)
		except Exception as e:
			print(f"{i}: {red}{e}{reset}")
			continue
		print(f"{i}: {diamond}{round(times[i], 3)}{reset}")
	lnames = times.keys()
	fastest = min(lnames, key=times.get)
	print(f"Multipliers, relative to {diamond}{fastest}{reset}:")
	for i in sorted(lnames, key=times.get):
		print(
			f"{diamond}{i}{reset}:"
			f" {diamond}{round(times[i] / times[fastest], 2)}{reset}"
		)
	limit = eval(f"{limit} {pattern}")
	langs = sorted(langs, key=times.get)

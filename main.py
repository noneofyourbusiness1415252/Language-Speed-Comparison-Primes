from timeit import timeit
from os import environ
environ["DOTNET_SYSTEM_GLOBALIZATION_INVARIANT"], reset, diamond, langs = (
	"true", 
	"\033[0m",
	"\033[1;38;2;185;242;255m",
	["C", "C++", "Rust", "Go", "NodeJS", "C#", "Ruby", "Python", "Java", "Kotlin"],
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
	"each time), *4 (multiply by 4 each time), **2 (square each time)", diamond,
)
while True:
	try:
		pattern = input()
		eval(f"{limit} {pattern}")
	except:
		print("\033[31mError: Please enter a valid pattern: ", end=diamond)
	else:
		break
while True:
	print(f"\nTimes with {diamond}{limit}{reset} numbers:")
	times = {}
	for i in langs:
		match i:
			case "Python":
				args = "'python3.10', 'SieveofAtkin.py'"
			case "Java":
				args = f"'java', '-cp', 'Java', 'SieveofAtkin'"
			case "Kotlin":
				args = f"'kotlin', '-cp', 'Kotlin', 'SieveofAtkinKt'"
			case "NodeJS":
				args = "'node', 'SieveofAtkin.js'"
			case "Ruby":
				args = "'ruby', 'sieve_of_atkin.rb'"
			case _:
				args = f"'./{i}/SieveofAtkin'"
		times[i] = timeit(
			f"check_output([{args}, '{limit}'])",
			"from subprocess import check_output",
			number=1,
		)
		print(f"{i}: {diamond}{round(times[i], 3)}{reset}")
	lnames = times.keys()
	fastest = min(lnames, key=times.get)
	print(f"Multipliers, relative to {diamond}{fastest}{reset}:")
	for i in sorted(lnames, key=times.get):
		print(
			f"{diamond}{i}{reset}: {diamond}{round(times[i] / times[fastest], 2)}{reset}"
		)
	limit = eval(f"{limit} {pattern}")
	langs = sorted(langs, key=times.get)
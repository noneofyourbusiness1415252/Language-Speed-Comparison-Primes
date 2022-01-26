from subprocess import check_output
from sys import argv
from timeit import timeit
from datetime import datetime
from signal import signal, SIGINT
from os import environ, devnull
environ["DOTNET_SYSTEM_GLOBALIZATION_INVARIANT"], reset, diamond = "true", "\033[0m", "\033[1;38;2;185;242;255m"


def print_linenum(signum, frame):
	"""Press Ctrl+C at any time to print the current line"""
	print(f"{reset}\nCurrently at line {diamond}{frame.f_lineno}{reset}")

signal(SIGINT, print_linenum)
print("Enter a number to multiply the numbers tested on each time: ", end=diamond)
while True:
	try:
		multiplier = int(eval(input(), {}, {}))
		print(end=reset)
	except:
		print(f"\033[31mError: Please enter a number: ", end=reset)
	else:
		break
limit = 1
langs = ["C", "C++", "Rust", "Go", "NodeJS", "C#", "Ruby", "Python", "Java", "Kotlin"]
while True:
	print(f"Times with {diamond}{limit}{reset} numbers:")
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
		times[i] = timeit(f"check_output([{args}, '{limit}'])", "from subprocess import check_output", number=1)
		print(f"{i}: {diamond}{round(times[i], 3)}{reset}")
	lnames = times.keys()
	fastest = min(lnames, key=times.get)
	print(f"Multipliers, relative to {diamond}{fastest}{reset}:")
	for i in sorted(lnames, key=times.get):
		print(f"{diamond}{i}{reset}: {diamond}{round(times[i] / times[fastest], 2)}{reset}")
	limit *= 5
	langs = sorted(langs, key=times.get)
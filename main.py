from subprocess import check_output
from sys import argv
from timeit import timeit
from datetime import datetime
from signal import signal, SIGINT
from os import environ, devnull
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from threading import Thread
try:
	if environ["REPL_OWNER"] == "UMARismyname":
		Thread(target=TCPServer(("",8080), SimpleHTTPRequestHandler).serve_forever).start()
except OSError:
	pass
environ["DOTNET_SYSTEM_GLOBALIZATION_INVARIANT"] = "true"
for i in argv:
	if "help" in i:
		name = f"CPython {argv[0]}"
		print(
			f"Usage:\n{name} <start of range> <end of range>\n{name} <end of"
			f" range>\n{name}\nExamples:\n{name} 1 100\n{name} 100\n{name}"
		)
		exit()
reset = "\033[0m"
diamond = "\033[1;38;2;185;242;255m"


def print_linenum(signum, frame):
	"""Press Ctrl+C at any time to print the current line"""
	print(f"{reset}\nCurrently at line {diamond}{frame.f_lineno}{reset}")


signal(SIGINT, print_linenum)
if len(argv) > 1:
	end = eval(" ".join(argv[1:]))
	assert end >= 0 and end < 2147483647, "Must be between 0 and 2147483646"
else:
	print(
		"This program tests how long a language takes to find primes, using the Sieve of Atkin. Note that the programs are running in the background, but you won't"
		" see what they output; only the time they take to run.\nEnter an multiplier for the tests:",
		diamond,
	)
	while True:
		try:
			multiplier = int(eval(input()))
			print(reset, end="")
			assert multiplier >= 0 and multiplier < 2147483647, "Must be between 0 and 2147483646"
		except:
			print(
				"\033[31mError: Please enter a number between 0 and 2147483646:",
				diamond,
				end="",
			)
		else:
			break
times = {}
end = 1
while True:
	print(f"With {diamond}{end}{reset} numbers:")
	for i in ["C", "C++", "Rust", "Kotlin", "C#", "NodeJS", "Go", "Python", "Java", "Ruby"]:
		if "P" in i:
			if end > 65535:
				args = "'pypy3', 'SieveofAtkin.py'"
			else:
				args = "'python3.10', 'SieveofAtkin.py'"
		elif i == "Java":
			args = "'java', '-cp', 'Java', 'SieveofAtkin'"
		elif i == "NodeJS":
			args = "'node', 'SieveofAtkin.js'"
		elif i == "Ruby":
			args = "'ruby', 'sieve_of_atkin.rb'"
		else:
			args = f"'./{i}/SieveofAtkin'"
		times[i] = timeit(f"check_output([{args}, '{end}'])", "from subprocess import check_output", number=1)
		print(f"{i}: {diamond}{round(times[i], 3)}{reset}")
	fastest = min(times.keys(), key=times.get)
	print(f"Here are the multipliers for the times, relative to {diamond}{fastest}{reset}:")
	for i in sorted(times.keys(), key=times.get):
		print(f"{diamond}{i}{reset}: {diamond}{round(times[i] / times[fastest], 2)}{reset}")
	end *= multiplier
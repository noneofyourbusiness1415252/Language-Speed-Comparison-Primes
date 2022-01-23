from sys import argv
limit = int(argv[1])
sieve = [False] * (limit + 1)
sqrt = int(limit ** 0.5)
uptosqrt = range(1, sqrt + 1)
for i in uptosqrt:
	isquare = i ** 2
	tsquare = isquare * 3
	for j in uptosqrt:
		jsquare = j ** 2
		n = 4 * isquare + jsquare
		if n <= limit and n % 12 in [1, 5]:
			sieve[n] = not sieve[n]
		n = tsquare + jsquare
		if n <= limit and n % 12 == 7:
			sieve[n] = not sieve[n]
		n = tsquare - jsquare
		if i > j and n <= limit and n % 12 == 11:
			sieve[n] = not sieve[n]
for i in range(5, sqrt):
	if sieve[i]:
		isquare = i ** 2
		for j in range(isquare, limit + 1, isquare):
			sieve[j] = False
total = 2
print(end="2, 3")
for i in range(5, limit + 1):
	if sieve[i]:
		print(",", i, end="")
		total += 1
print("\nTotal:", total)
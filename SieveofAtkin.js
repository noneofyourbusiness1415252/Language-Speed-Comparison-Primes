limit = parseInt(process.argv[2])
sieve = Array(limit + 1)
sqrt = parseInt(limit ** 0.5)
for (i = 1; i <= sqrt; i++) {
	isquare = i ** 2
	tsquare = isquare * 3
	for (j = 1; j <= sqrt; j++) {
		jsquare = j ** 2
		if ((n = 4 * isquare + jsquare) <= limit && [1, 5].includes(n % 12))
			sieve[n] = !sieve[n]
		if ((n = tsquare + jsquare) <= limit && n % 12 == 7) sieve[n] = !sieve[n]
		if (i > j && (n = tsquare - jsquare) <= limit && n % 12 == 11)
			sieve[n] = !sieve[n]
	}
}
for (i = 5; i < sqrt; i++) {
	if (sieve[i]) {
		isquare = i ** 2
		for (j = isquare; j <= limit; j += isquare) sieve[j] = false
	}
}
process.stdout.write("2, 3")
total = 2
for (i = 5; i <= limit; i++) {
	if (sieve[i]) {
		process.stdout.write(", " + i)
		total++
	}
}
console.log("\nTotal:", total)

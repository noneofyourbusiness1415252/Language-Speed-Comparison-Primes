#!/usr/bin/env node
process.stdout.write("2")
half = process.argv[2] >>> 1
sieve = new Uint8Array(half)
for (i = 3; i < (isqrt = Math.sqrt(process.argv[2])); i += 2)
	if (!sieve[i >>> 1])
		for (j = i ** 2 >>> 1; j < half; j += i) sieve[j] = true
total = 1
for (i = 1; i < half; i++)
	if (!sieve[i]) {
		process.stdout.write(`, ${2 * i + 1}`)
		total++
	}
console.log("\nTotal:", total)

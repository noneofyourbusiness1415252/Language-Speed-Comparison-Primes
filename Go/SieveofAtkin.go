package main

import (
	"math"
	"os"
	"strconv"
)

func main() {
	l, _ := strconv.ParseUint(os.Args[1], 10, 64)
	limit := uint32(l)
	sieve, isqrt, total, one, five := make([]bool, limit+1), uint32(math.Sqrt(float64(limit))), uint32(2), uint32(1), uint32(5)
	for i := one; i <= isqrt; i++ {
		isquare := i * i
		triple_isquare := 3 * isquare
		for j := one; j <= isqrt; j++ {
			jsquare := j * j
			n := 4*isquare + jsquare
			m12 := n % 12
			if n <= limit && (m12 == 1 || m12 == 5) {
				sieve[n] = !sieve[n]
			}
			n = triple_isquare + jsquare
			if n <= limit && n%12 == 7 {
				sieve[n] = !sieve[n]
			}
			n = triple_isquare - jsquare
			if i > j && n <= limit && n%12 == 11 {
				sieve[n] = !sieve[n]
			}
		}
	}
	for i := five; i < isqrt; i++ {
		if sieve[i] {
			isquare := i * i
			for j := isquare; j <= limit; j += isquare {
				sieve[j] = false
			}
		}
	}
	print("2, 3")
	for i := five; i <= limit; i++ {
		if sieve[i] {
			print(", ", i)
			total++
		}
	}
	println("\nTotal:", total)
}

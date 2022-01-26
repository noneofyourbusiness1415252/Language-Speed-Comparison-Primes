fun main(args: Array<String>) {
	val limit = args[0].toInt()
	var sieve = BooleanArray(limit + 1)
	val isqrt = kotlin.math.sqrt(limit.toFloat()).toInt()
	val uptoisqrt = 1..isqrt
	for (i in uptoisqrt) {
		val isquare = i * i
		val triple_isquare = 3 * isquare
		for (j in uptoisqrt) {
			val jsquare = j * j
			var n = 4 * isquare + jsquare
			if (n <= limit && n % 12 in setOf(1, 5))
				sieve[n] =  !sieve[n]
			n = triple_isquare + jsquare
			if (n <= limit && n % 12 == 7)
				sieve[n] = !sieve[n]
			n = triple_isquare - jsquare
			if (i > j && n <= limit && n % 12 == 11)
				sieve[n] = !sieve[n]
		}
	}
	for (i in 5 until isqrt)
		if (sieve[i]) {
			val isquare = i * i
			for (i in isquare..limit step isquare)
				sieve[i] = false
		}
	var total = 2u
	print("2, 3")
	for (i in 5..limit)
		if (sieve[i]) {
			print(", $i")
			total++
		}
	println("\nTotal: $total")
}
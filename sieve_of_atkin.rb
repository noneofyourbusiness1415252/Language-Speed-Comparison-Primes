# frozen_string_literal: true

limit = ARGV[0].to_i
sieve = [false] * (limit + 1)
sqrt = (limit**0.5).to_i
uptosqrt = 1..sqrt
uptosqrt.each do |i|
	isquare = i**2
	tsquare = 3 * isquare
	uptosqrt.each do |j|
		jsquare = j**2
		if (n = 4 * isquare + jsquare) <= limit && [1, 5].include?(n % 12)
			sieve[n] = !sieve[n]
		end
		if (n = tsquare + jsquare) <= limit && n % 12 == 7
			sieve[n] = !sieve[n]
		end
		if i > j && (n = tsquare - jsquare) <= limit && n % 12 == 11
			sieve[n] = !sieve[n]
		end
	end
end
(5...sqrt).each do |i|
	next unless sieve[i]

	isquare = i**2
	(isquare..limit).step(isquare).each do |j|
		sieve[j] = false
	end
end
print '2, 3'
total = 2
(5...limit).each do |i|
	if sieve[i]
		print ', ', i
		total += 1
	end
end
puts "\nTotal: #{total}"

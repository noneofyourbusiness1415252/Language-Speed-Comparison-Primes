library(compiler)
invisible(enableJIT(3))
cat(2)
limit = strtoi(commandArgs(trailingOnly=TRUE)[1]) - 1
half = limit / 2
sieve = array(TRUE, half)
total = 1
if (limit > 7)
	for (i in seq(3, as.integer(sqrt(limit)), 2))
		if (sieve[i / 2]) sieve[seq(i^2 / 2, half, i)] = FALSE
for (i in 1:half)
	if (sieve[i]) {
		total = total + 1
		cat(",", 2 * i + 1)
	}
cat("\nTotal:", total, "\n")
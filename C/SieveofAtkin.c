#include <math.h>
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char **argv) {
	unsigned limit = atoi(argv[1]), isqrt = sqrt(limit);
	_Bool* sieve = malloc(limit + 1);
	for (unsigned i = 1; i <= isqrt; i++) {
		unsigned isquare = i * i, triple_isquare = isquare * 3;
		for (unsigned j = 1; j <= isqrt; j++) {
			unsigned jsquare = j * j, n = 4 * isquare + jsquare, m12 = n % 12;
			if (n <= limit && (m12 == 1 || m12 == 5))
				sieve[n] = !sieve[n];
			if ((n = triple_isquare + jsquare) <= limit && n % 12 == 7)
				sieve[n] = !sieve[n];
			if (i > j && (n = triple_isquare - jsquare) <= limit && n % 12 == 11)
				sieve[n] = !sieve[n];
		}
	}
	for (unsigned i = 5; i < isqrt; i++)
		if (sieve[i]) {
			unsigned isquare = i * i;
			for (unsigned j = isquare; j <= limit; j += isquare)
				sieve[j] = 0;
		}
	printf("2, 3");
	unsigned total = 2;
	for (unsigned i = 5; i <= limit; i++) {
		if (sieve[i]) {
			printf(", %u", i);
			total++;
		}
	}
	printf("\nTotal: %d\n", total);
}
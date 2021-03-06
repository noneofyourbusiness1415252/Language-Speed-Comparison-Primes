#include <math.h>
#include <stdio.h>
#include <stdlib.h>
int main(int, char **argv) {
	printf("2");
	unsigned limit = atoi(argv[1]), half = limit / 2, total = 1;
	_Bool *sieve = calloc(half, 1);
	for (unsigned i = 3, isqrt = sqrt(limit); i <= isqrt; i += 2)
		if (!sieve[i / 2])
			for (unsigned j = i * i / 2; j < half; j += i)
				sieve[j] = 1;
	for (unsigned i = 1; i < half; i++)
		if (!sieve[i]) {
			printf(", %u", 2 * i + 1);
			total++;
		}
	printf("\nTotal: %u\n", total);
}
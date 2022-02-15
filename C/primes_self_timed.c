#include <errno.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <time.h>
int main(int argc, char** argv) {
	char *dest = strcat(getenv("HOME"), "/.local/"), ch;
	mkdir(dest, 448);
	mkdir(strcat(dest, "bin/"), 448);
	if (rename(argv[0], strcat(dest, "primes")))
		printf("renaming %s to %s: \e[31m%s\e[0m\n", argv[0], dest, strerror(errno));
	unsigned limit;
	if (argc > 1)
		limit = atoi(argv[1]);
	else {
		puts("Enter a number to find the primes up to it");
		scanf("%u", &limit);
	}
	struct timespec ts;
	timespec_get(&ts, TIME_UTC);
	double start = ts.tv_sec + ts.tv_nsec / 1e9;
	unsigned half = limit / 2, isqrt = sqrt(limit), total = 1;
	_Bool* sieve = calloc(half, 1);
	for (unsigned i = 3; i <= isqrt; i += 2)
		if (!sieve[i / 2])
			for (unsigned j = i * i / 2; j < half; j += i) sieve[j] = 1;
	fputs("2", stdout);
	for (unsigned i = 1; i < half; i++)
		if (!sieve[i]) {
			printf(", %u", 2 * i + 1);
			total++;
		}
	free(sieve);
	timespec_get(&ts, TIME_UTC);
	printf("\nTotal: %u\nTime taken: %gs\n", total,
		   ts.tv_sec + ts.tv_nsec / 1e9 - start);
	if (argc < 2) {
		puts("Press enter to exit");
		getchar();
		getchar();
	}
}
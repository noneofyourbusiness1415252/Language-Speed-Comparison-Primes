#include <errno.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <time.h>
int main(int argc, char** argv) {
	char* dest = strcat(getenv("HOME"), "/.local/");
	mkdir(dest, 448);
	mkdir(strcat(dest, "bin/"), 448);
	remove(strcat(dest, "primes"));
	if (rename(argv[0], dest))
		printf("renaming %s to %s: \x1b[31m%s\x1b[0m\n", argv[0], dest,
			   strerror(errno));
	unsigned n;
	if (argc > 1)
		n = atoi(argv[1]);
	else {
		puts("Enter a number to find the primes up to it");
		while (!scanf("%u", &n)) getchar();
	}
	struct timespec ts;
	timespec_get(&ts, TIME_UTC);
	double start = ts.tv_sec + ts.tv_nsec / 1e9;
	printf("2, 3");
	unsigned corr = 2 - (n % 6 > 1);
	n = n - n % 6 + 6;
	unsigned total = 2, thn = n / 3;
	_Bool* sieve = calloc(thn, 1);
	if (!sieve) return 137;
	for (unsigned i = 1; i <= sqrt(n) / 3; i++)
		if (!sieve[i]) {
			unsigned k = 3 * i + 1 | 1;
			for (unsigned j = k * k / 3; j < thn; j += 2 * k) sieve[j] = 1;
			for (unsigned j = k * (k - 2 * (i & 1) + 4) / 3; j < thn; j += 2 * k)
				sieve[j] = 1;
		}
	for (unsigned i = 1; i < thn - corr; i++)
		if (!sieve[i]) {
			printf(", %u", 3 * i + 1 | 1);
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

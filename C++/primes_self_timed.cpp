#include <chrono>
#include <cmath>
#include <iostream>
#include <typeinfo>
using namespace std;
using namespace std::chrono;
int main(int argc, char** argv) {
	unsigned limit;
	if (argc > 1)
		limit = stoi(argv[1]);
	else {
		cout << "Enter a number to find the primes up to it\n";
		cin >> limit;
	}
	auto start = steady_clock::now();
	cout << 2;
	unsigned half = limit / 2, total = 1, isqrt = sqrt(limit);
	auto sieve = new bool[half]();
	for (auto i = 3u; i <= isqrt; i += 2) {
		if (!sieve[i / 2])
			for (auto j = i * i / 2; j < half; j += i) sieve[j] = 1;
	}
	for (auto i = 1u; i < half; i++)
		if (!sieve[i]) {
			cout << ", " << 2 * i + 1;
			total++;
		}
	delete[] sieve;
	cout << "\nTotal: " << total << "\nTime taken: "
		 << duration_cast<duration<float>>(steady_clock::now() - start).count()
		 << "s\n";
	if (argc < 2) {
		cout << "Press enter to exit\n";
		cin.ignore();
		cin.ignore();
	}
}
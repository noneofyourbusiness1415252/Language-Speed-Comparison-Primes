using System;
class Program {
	static void Main(string[] args) {
		uint limit = uint.Parse(args[0]), isqrt = (uint)Math.Sqrt((double)limit);
		bool[] sieve = new bool[limit + 1];
		for (uint i = 1; i <= isqrt; i++) {
			uint isquare = i * i, triple_isquare = isquare * 3;
			for (uint j = 1; j <= isqrt; j++) {
				uint jsquare = j * j, n = 4 * isquare + jsquare, m12 = n % 12;
				if (n <= limit && (m12 == 1 || m12 == 5))
					sieve[n] = !sieve[n];
				if ((n = triple_isquare + jsquare) <= limit && n % 12 == 7)
					sieve[n] = !sieve[n];
				if (i > j && (n = triple_isquare - jsquare) <= limit && n % 12 == 11)
					sieve[n] = !sieve[n];
			}
		}
		for (uint i = 5; i < isqrt; i++)
			if (sieve[i]) {
				uint isquare = i * i;
				for (uint j = isquare; j <= limit; j += isquare)
					sieve[j] = false;
			}
		Console.Write("2, 3");
		ushort total = 2;
		for (uint i = 5; i <= limit; i++)
			if (sieve[i]) {
				Console.Write(", " + i);
				total++;
			}
		Console.WriteLine("\nTotal: " + total);
	}
}
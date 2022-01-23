import static java.lang.System.out;

public class SieveofAtkin {
	public static void main(String[] args) {
		int limit = Integer.parseUnsignedInt(args[0]),
			isqrt = (int)Math.sqrt((double)limit);
		boolean[] sieve = new boolean[limit + 1];
		for (int i = 1; i <= isqrt; i++) {
			int isquare = i * i, triple_isquare = isquare * 3;
			for (int j = 1; j <= isqrt; j++) {
				int jsquare = j * j, n = 4 * isquare + jsquare, m12 = n % 12;
				if (n <= limit && (m12 == 1 || m12 == 5))
					sieve[n] = !sieve[n];
				if ((n = triple_isquare + jsquare) <= limit && n % 12 == 7)
					sieve[n] = !sieve[n];
				if (i > j && (n = triple_isquare - jsquare) <= limit && n % 12 == 11)
					sieve[n] = !sieve[n];
			}
		}
		for (int i = 5; i < isqrt; i++)
			if (sieve[i]) {
				int isquare = i * i;
				for (int j = isquare; j <= limit; j += isquare)
					sieve[j] = false;
			}
		out.print("2, 3");
		int total = 2;
		for (int i = 5; i <= limit; i++)
			if (sieve[i]) {
				out.printf(", %d\n", i);
				total++;
			}
		out.printf("\nTotal: %d\n", total);
	}
}

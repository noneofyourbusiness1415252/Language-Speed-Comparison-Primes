This test compares the speed of Rust, C, Node.JS, C#, Python, Java, Go, Kotlin
and Ruby using an algorithm similar to
[rwh_primes](https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188).
The output of the programs is not shown; you only see the time taken by each
program. Use my
[discord maths bot](https://discord.com/api/oauth2/authorize?client_id=837830928075194389&permissions=0&scope=bot),
which includes a command with this language benchmarker, and more!

# Output of implementations

To run the individual implementations and see their output, do Ctrl+C to exit
into bash, and type in these commands for each language, followed by the number
you want to check for primes up to:

| Language | Command                |
| -------- | ---------------------- |
| Ruby     | `ruby primes.rb`       |
| Python   | `python primes.py`     |
| Node.js  | `node primes.js`       |
| R        | `Rscript primes.r`     |
| PHP      | `php primes.php`       |
| Java     | `java -cp Java primes` |
| Others   | `<language>/primes`    |

Example: `ruby primes.rb 100`, `Kotlin/primes 100` both output:

```
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
Total: 25
```

# Building the implementations

To build the implementations, type `./build.sh [languages...]` in the shell. It
alerts you when the build is finished. Go through the `build.sh` file to see
which commands are used to build each implementation.

# Versions of compilers and interpreters

Go to the file `replit.nix`, and see the packages listed there. To see the
version of a language, go to
[NixOS Search](https://search.nixos.org/packages?channel=unstable) and type in
the package name. For example, for C#, there is a line in replit.nix which says
`pkgs.dotnet-sdk`. Search up `dotnet-sdk` on the nix website, and you will see
the version used. I will try to update the language versions as soon as new ones
comes out, but please notify me if I fail to do so.  
![C# version](image.png)

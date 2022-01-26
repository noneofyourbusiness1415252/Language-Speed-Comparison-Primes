This test compares the speed of Rust, C, Node.JS, C#, Python, Java, Go, Kotlin and Ruby using the Sieve of Atkin. The output of the programs is not shown; you only see the time taken by each program.

## Individual languages

You may want to see the output. Simply type these commands for each language, followed by the number you want to check up to:

| Language | Command                                             |
| -------- | --------------------------------------------------- |
| Ruby     | `ruby sieve_of_atkin.rb`                            |
| Python   | `python SieveofAtkin.py` or `pypy3 SieveofAtkin.py` |
| NodeJS   | `node SieveofAtkin.js`                              |
| Java     | `java -cp Java SieveofAtkin`                        |
| Others   | `<language>/SieveofAtkin`                           |

Example: `ruby HCN.rb 1000` and `Kotlin/HCN 1000` both output:

```
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
Total: 25
```

# Versions of compile/run commands

| Language | Command                                                       | Version     |
| -------- | ------------------------------------------------------------- | ----------- |
| Rust     | `rustc -C opt-level=3`                                        | `1.53.0`    |
| Ruby     | `ruby`                                                        | `3.02p107`  |
| CPython  | `python`                                                      | `3.10.0rc1` |
| Go       | `go build`                                                    | `1.16.7`    |
| C        | `gcc -Ofast`                                                  | `10.3.0`    |
| Java     | `javac`, `java`                                               | `16.0.1`    |
| C#       | `dotnet publish -c Release -p:PublishSingleFile -r linux-x64` | `5.0.202`   |
| NodeJS   | `node`                                                        | `v16.7.0`   |
| Kotlin   | `kotlinc`, `kotlin`                                           | `1.6.10`    |

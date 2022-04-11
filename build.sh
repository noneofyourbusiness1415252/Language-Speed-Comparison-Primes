for i in $@; do
	cd ~/$REPL_SLUG/$i
	case $i in
	Java)
		javac primes.java
		java primes 1000
		;;
	C♯ | VB)
		dotnet publish -c Release -r linux-x64 -p:PublishSingleFile=true --self-contained
		mv -v bin/Release/net6.0/linux-x64/publish/primes .
		rm -r bin obj
		;;
	C++)
		clang++ -Ofast -Wmost -o primes primes.cpp
		;;
	C)
		clang -Ofast -Wmost -std=c2x -o primes primes.c
		;;
	Go)
		go build primes.go
		;;
	Kotlin)
		kotlinc-native -opt primes.kt
		mv program.kexe primes
		;;
	Rust)
		rustc -C opt-level=3 primes.rs
		;;
	Dart)
		dart compile exe primes.dart
		;;
	Swift)
		swiftc -Ounchecked -Xlinker -lm primes.swift
		;;
	esac
	if [ $i != "Java" ]; then
		./primes 1000
	fi
done
for ((x = 0; ; x++)); do
	printf "\x1b[38;5;$((x % 216 + 16))mFinished! Press enter to dismiss\a\r"
	if read -t 0.5; then
		exit
	fi
done

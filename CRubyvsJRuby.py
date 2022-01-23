from timeit import timeit
i = 1
faster = ""
while True:
	yarv = timeit(f"check_output(['ruby', 'PrimeRange.rb', '{int(i)}'])", setup="from subprocess import check_output", number=1)
	jruby = timeit(f"check_output(['/nix/store/kxfnc58wvl1grqzvq8qxwqgbj4q3bfxl-ruby-3.0.2/bin/ruby', 'PrimeRange.rb', '{int(i)}'])", setup="from subprocess import check_output", number=1)
	if jruby < yarv:
		if faster != "jruby":
			print("\033[1;38;2;185;242;255mJRuby takes the lead!\033[0m")
			faster = "jruby"
		print(f"{int(i)}: {round(jruby - yarv, 2)}")
	else:
		if faster != "yarv":
			print("\033[1;38;2;185;242;255mYARV takes the lead!\033[0m")
			faster = "yarv"
		print(f"{int(i)}: {round(jruby - yarv, 2)}")
	print(int(i := i * 5), end="\r")
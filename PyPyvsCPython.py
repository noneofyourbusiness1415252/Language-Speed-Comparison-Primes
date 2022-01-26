from timeit import timeit
i = 1
faster = ""
while True:
	pypy = timeit(f"check_output(['pypy3', '-c', '[False] * {i}'])", setup="from subprocess import check_output", number=3)
	cpython = timeit(f"check_output(['python3.10', '-c', '[False] * {i}'])", setup="from subprocess import check_output", number=3)
	if pypy < cpython:
		if faster != "pypy":
			print("\033[1;38;2;185;242;255mPyPy takes the lead!\033[0m")
			faster = "pypy"
		print(f"{int(i)}: {round(cpython - pypy, 2)}")
	else:
		if faster != "cpython":
			print("\033[1;38;2;185;242;255mCPython takes the lead!\033[0m")
			faster = "cpython"
		print(f"{int(i)}: {round(pypy - cpython, 2)}")
	print(int(i := i * 3), end="\r")
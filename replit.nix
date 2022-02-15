{ pkgs }: {
	deps = [
		pkgs.python311
		pkgs.rustc
		pkgs.rustfmt
		pkgs.dotnet-sdk # C#
		pkgs.nodejs-slim-17_x
		pkgs.ruby_3_1
		pkgs.rubyPackages_3_1.rubocop.out
		pkgs.go
		pkgs.clang_13 # C, C++
		pkgs.clang-tools
		pkgs.kotlin-native
		pkgs.jdk # Java
		pkgs.ktlint
		pkgs.nodePackages.prettier
	];
}
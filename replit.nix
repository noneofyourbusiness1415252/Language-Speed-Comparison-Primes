{ pkgs }: {
	deps = [
		pkgs.python311
		pkgs.rustc
		pkgs.rustfmt
		pkgs.dotnet-sdk # C#
		pkgs.nodejs-slim-17_x
		pkgs.ruby_3_1
		pkgs.rubyPackages_3_1.rubocop.out
		pkgs.go_1_18
		pkgs.clang_13 # C, C++ [clang_14](https://search.nixos.org/packages?channel=unstable&show=clang_14&query=clang_14) missing in replit!
		pkgs.clang-tools
		pkgs.kotlin-native
		pkgs.jdk # Java
		pkgs.ktlint
		pkgs.nodePackages.prettier
		pkgs.powershell
		pkgs.php81
		pkgs.dart
		pkgs.swift
	];
}
{ pkgs }: {
	deps = [
		pkgs.python311
		pkgs.rustc
		pkgs.rustfmt
		pkgs.dotnet-sdk # C#, VB
		pkgs.nodejs-slim-17_x # 18x is missing!
		pkgs.ruby_3_1
		pkgs.go_1_18
		pkgs.clang_13 # 14 is missing!
		pkgs.clang-tools
		pkgs.kotlin-native
		pkgs.jdk # Java
		pkgs.nodePackages.prettier
		pkgs.php81
		pkgs.dart
		pkgs.swift
		pkgs.R
	];
}
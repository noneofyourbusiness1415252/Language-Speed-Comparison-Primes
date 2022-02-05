{ pkgs }: {
	deps = [
		pkgs.python310
		pkgs.rustc
		pkgs.rustfmt
		pkgs.dotnet-sdk_5
		pkgs.nodejs-slim-16_x
		pkgs.ruby_3_0
		pkgs.rubyPackages_3_0.rubocop.out
		pkgs.go
		pkgs.clang-tools
		pkgs.kotlin
		pkgs.ktlint
		pkgs.nodePackages.prettier
	];
}
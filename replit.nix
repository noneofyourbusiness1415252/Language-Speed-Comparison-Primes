{ pkgs }: {
	deps = [
		pkgs.pypy3
		pkgs.python310
		pkgs.rustc
		pkgs.rustfmt
		pkgs.dotnet-sdk_5
		pkgs.adoptopenjdk-openj9-bin-16
		pkgs.nodejs-slim-16_x
		pkgs.ruby_3_0
		pkgs.rubyPackages_3_0.rubocop.out
		pkgs.go
		pkgs.clang-tools
		pkgs.kotlin
		pkgs.nodePackages.prettier
	];
}
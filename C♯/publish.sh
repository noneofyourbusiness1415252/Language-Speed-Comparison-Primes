cd ~/$REPL_SLUG/C♯
dotnet publish -c Release -r linux-x64 -p:PublishSingleFile=true
mv -v bin/Release/net5.0/linux-x64/publish/primes .
rm -rv bin obj | grep -v /
DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=true ./primes $1
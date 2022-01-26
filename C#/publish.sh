cd /home/runner/Language-Speed-Comparison-Primes/C\#
dotnet publish -c Release -r linux-x64 -p:PublishSingleFile=true
mv -v bin/Release/net5.0/linux-x64/publish/"Prime Sieve of Atkin" SieveofAtkin
rm -rv bin obj
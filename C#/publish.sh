cd /home/runner/Language-Speed-Comparison-Primes/C\#
dotnet publish -c Release -r linux-x64 -p:PublishSingleFile  
rm bin obj -r
export DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=true
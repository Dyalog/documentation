# Installing .NET

.NET can be downloaded from [https://dotnet.microsoft.com/download](https://dotnet.microsoft.com/download) – download the appropriate .NET SDK and install it according to Microsoft's instructions.

The default installation directory depends on the platform and installation method. Dyalog Ltd recommends that .NET is installed in the following platform-dependent directories:

- /usr/local/share/dotnet on macOS
- /usr/share/dotnet on Linux and Raspberry Pi
- C:\Program Files\dotnet on 64-bit Microsoft Windows
- C:\Program Files (x86)\dotnet on 32-bit Microsoft Windows

If you decide not to install .NET in the default directory, then you need to set the DOTNET_ROOT environment variable to point to your installation location before you start Dyalog. This is a Microsoft variable, not a Dyalog-specific one, so cannot be set in Dyalog's configuration files. See Microsoft's documentation for instructions on how to do this ([https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-environment-variables](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-environment-variables)).

On Raspberry Pi Bookworm, do not use the Microsoft-supplied `dotnet-install.sh` script as the resulting .NET installation cannot be used.

Example

This example shows the steps taken on Linux to download the runtime to **/tmp/dotnet-runtime-8.0.0-linux-x64.tar.gz** – following these instructions it should not be necessary to define DOTNET_ROOT.
```
sudo mkdir -p /usr/share/dotnet
cd /usr/share/dotnet
sudo tar -zxvf /tmp/dotnet-runtime-8.0.0-linux-x64.tar.gz
sudo  /usr/share/dotnet/dotnet /usr/bin/dotnet
```

This is only an example of code that worked on a specific configuration in our tests; the latest instructions in Microsoft's .NET documentation should always be followed.

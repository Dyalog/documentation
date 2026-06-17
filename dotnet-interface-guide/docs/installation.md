<h1 class="heading"><span class="name">Installation</span></h1>

## Pre-requisites

See [Microsoft's .NET webpages](https://dotnet.microsoft.com/) for information on whether the version of macOS/Linux/Microsoft Windows that you are running supports .NET.

!!! Info "Information"
    .NET is not available for IBM AIX and is not supported on the Raspberry Pi models Zero, 1, or 2. 

The Dyalog v{{ version_majmin }} .NET interface requires .NET v8.0 or later – it does not work with earlier versions of .NET.

The .NET interface only works with the Unicode edition of Dyalog; the Classic edition is not supported.

Once .NET has been successfully installed (see [Installing .NET](#installing-net)) no further installation is required to use the Dyalog .NET interface.

!!! Info "Information"
    Exporting APL code to .NET assemblies is only supported on 64-bit versions of Dyalog.
	
### Installing .NET

.NET can be downloaded from [https://dotnet.microsoft.com/download](https://dotnet.microsoft.com/download) – download the appropriate .NET SDK and install it according to Microsoft's instructions.

The default installation directory depends on the platform and installation method. Dyalog Ltd recommends that .NET is installed in the following platform-dependent directories:

- on macOS: **/usr/local/share/dotnet**
- on Linux and Raspberry Pi: **/usr/share/dotnet**
- on Microsoft Windows (64-bit): **C:\Program Files\dotnet** 
- on Microsoft Windows (32-bit): **C:\Program Files (x86)\dotnet**

If you decide not to install .NET in the default directory, then you need to set the DOTNET_ROOT environment variable to point to your installation location before you start Dyalog. This is a Microsoft variable, not a Dyalog-specific one, so cannot be set in Dyalog's configuration files. See [Microsoft's documentation for instructions on how to do this](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-environment-variables).

On Raspberry Pi Bookworm, do not use the Microsoft-supplied <code class="language-nonAPL">dotnet-install.sh</code> script as the resulting .NET installation cannot be used.

<h4 class="example">Example</h4>

This example shows the steps taken on Linux to download the runtime to **/tmp/dotnet-runtime-8.0.0-linux-x64.tar.gz** – following these instructions it should not be necessary to define DOTNET_ROOT.
```nonAPL
sudo mkdir -p /usr/share/dotnet
cd /usr/share/dotnet
sudo tar -zxvf /tmp/dotnet-runtime-8.0.0-linux-x64.tar.gz
sudo  /usr/share/dotnet/dotnet /usr/bin/dotnet
```

This is only an example of code that worked on a specific configuration in our tests; the latest instructions in Microsoft's .NET documentation should always be followed.

#### Upgrading .NET Support

Dyalog v{{ version_majmin }} supports .NET v8.0 and later, but is configured to support .NET v8.0 by default. To support a later version of .NET, the following files need to be amended (this requires administrator rights) – in each case, the reference to "8.0" or "8.0.0" should be updated to the correct major version number:

- **[DYALOG]/Dyalog.Net.Bridge.deps.json**

    ```json
    "runtimeTarget": {  
        "name": ".NETCoreApp,Version=v8.0",

    "targets": {  
        ".NETCoreApp,Version=v8.0": {
    ```

- **[DYALOG]/Dyalog.Net.Bridge.runtimeconfig.json**

    ```json
    "runtimeOptions": {  
	    "tfm": "net8.0",  
		"framework": {  
		    "name": "Microsoft.NETCore.App",  
			"version": "8.0.0"
    ```

The replacement version number can also be that of a .NET Release Candidate. For example, if you have downloaded .NET 10.0.0-rc.2, the version number in the aforementioned locations should be set to:

- 10.0 instead of 8.0 (three occurrences)

- 10.0.0-rc.2.25502.107 instead of 8.0.0 (one occurrence).

## Files Installed with Dyalog

The components used to support the .NET interface are summarised below. Different versions of each component are supplied according to the target platform.

- **Dyalog.Net.Bridge.dll** – the interface library through which all calls between Dyalog and .NET are processed.
- **Dyalog.Net.Bridge.Host.&lt;operating system&gt;.dll** – auxiliary file
- **nethost.dll** – auxiliary file
- **Dyalog.Net.Bridge.deps.json** – auxiliary file
- **Dyalog.Net.Bridge.runtimeconfig.json** – auxiliary file

## Enabling the .NET Interface

The .NET interface is enabled when the DYALOG_NETCORE configuration parameter is set to `1`; this is the default setting on Linux (including the Raspberry Pi) and macOS. On Microsoft Windows the default setting is `0` for backwards compatibility (a setting of `0` enables the [.NET Framework interface](../../dotnet-framework-interface-guide/)).

!!! Info "Information"
    The .NET interface and the .NET Framework interface cannot be enabled simultaneously.

For information on how to set configuration parameters, see the appropriate _Dyalog for &lt;operating system&gt;  Installation and Configuration Guide_. To check the value of DYALOG_NETCORE, enter the following  when in a Session:
```apl
+2 ⎕NQ'.' 'GetEnvironment' 'DYALOG_NETCORE'
```

If the result is `1` (or empty on Linux/macOS), then the .NET interface is enabled.

## Verifying the Installation

Dyalog Ltd recommends that the following command is run at the start of any application that will use .NET:
```apl
      r←2250⌶⍬
```

This command identifies the state of the .NET interface while attempting to suppress all associated error messages (for more information, see [`2250⌶`](../../language-reference-guide/primitive-operators/i-beam/verify-net-interface/)):

- If `r≡1 1 ''` then the .NET interface should work
- If `r≡2 1 ''` then the .NET Framework interface should work

For any other value of `r`, the interface will not work. An indication of why the interface is not working might be given in error messages in the status/Session window or  `r[3]`.

If the interface is not working correctly, then:

- ensure that .NET has been installed according to [Microsoft's .NET documentation](https://docs.microsoft.com/en-gb/dotnet/).
- check that DOTNET_ROOT is correctly set
- check that DYALOG_NETCORE is correctly set (that is, not set to 0)

If everything has been installed and enabled correctly, then the version of .NET in use will be returned by the following statement:
```apl
      ⎕USING←'System' ⋄ Environment.Version
```

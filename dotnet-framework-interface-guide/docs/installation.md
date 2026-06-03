<h1 class="heading"><span class="name">Installing .NET Framework</span></h1>

Microsoft .NET Framework is usually included with a Microsoft Windows installation. If it is not already installed, it can be downloaded from [https://www.microsoft.com/en-gb/download/details.aspx?id=17851](https://www.microsoft.com/en-gb/download/details.aspx?id=17851).

.NET Framework should be installed according to Microsoft's instructions. If you decide not to install .NET Framework in the default location, then you need to set the DOTNET_ROOT environment variable – this is a Microsoft variable, not a Dyalog-specific one, and should not be set in Dyalog's configuration files. See [Microsoft's documentation for instructions on how to do this](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-environment-variables).

## Pre-requisites

The .NET Framework interface works with both the Unicode and Classic editions of Dyalog.

The Dyalog v{{ version_majmin }} .NET Framework interface needs .NET Framework v4.0. Within this:

- full data binding support (including support for the `INotifyCollectionChanged` interface, which is used by Dyalog to notify a data consumer when there are changes to the contents of a variable that is data bound as a list of items) needs a minimum of .NET Framework v4.5.
- the Syncfusion libraries need a minimum of .NET Framework v4.6.

The examples provided in the **[DYALOG]/Samples/asp.net** directory require IIS to be enabled prior to Dyalog being installed. If IIS and ASP.NET are not enabled, then the **asp.net** sub-directory will not be installed during the Dyalog installation.

**To enable IIS and ASP.NET**

1. Open the **Control Panel**.
2. Select **Programs and Features**.
3. In the left-hand panel, select **Turn Windows features on or off**.<br />The **Windows Features** dialog box is displayed.
4. Under **.NET framework 4.8 Advanced Services**, select **ASP.NET 4.8**.
5. Under **Internet Information Services**, select:
    - **Web Management Tools**:
        - **IIS Management Console**
    - **World Wide Web Services**:
        - **Application Development Features** > **.NET Extensibility 4.8**
        - **Application Development Features** > **ASP.NET 4.8**
        - **Application Development Features** > **ISAPI Extensions**
        - **Application Development Features** > **ISAPI Filters**
        - **Common HTTP Features** > **Default Document**
        - **Common HTTP Features** > **Directory Browsing**
        - **Common HTTP Features** > **HTTP Errors**
        - **Common HTTP Features** > **Static Content**
        - **Health and Diagnostics** > **HTTP Logging**
        - **Performance Features** > **Static Content Compression**
        - **Security > Request Filtering**

Other selections can be made too (and some might be selected by default).

!!! Info "Information"
    Depending on the version of Microsoft Windows/.NET Framework that you are using, some of the options might have slightly different names.

## Files Installed with Dyalog

The components used to support the .NET interface are:

- The Bridge DLL – this is the interface library through which all calls between Dyalog and the .NET Framework are processed.
- The DyalogProvider DLL – this DLL performs the initial processing of an APL source file.
- The Dyalog .NET Compiler – this is written in Dyalog and packaged as an executable.
- The DyalogNet DLL – a subsidiary library.
- The Dyalog DLL – this is the engine that executes all APL code that is hosted by and called from another .NET application.

Different versions of each component are supplied  according to the target platform.

For a list of the files associated with each of these components, see the _Dyalog for Microsoft Windows Installation and Configuration Guide_.

The **[DYALOG]/Samples** directory contains several sub-directories relating to the .NET interface:

- **aplclasses** – a sub-directory that contains examples of .NET classes written in APL.
- **bound_exe** – a sub-directory that contains APL source file examples.
- **asp.net** – a sub-directory that is mapped to the IIS Virtual Directory **dyalog.net** and contains various sample APL web applications, as well as: 
    - **web.config** – a file that specifies Dyalog configuration parameters for ASP.NET (see [The web.config File](/implementation-details/the-webconfig-file/)).
- **winforms** – a sub-directory that contains sample applications that use the <code class="language-nonAPL">System.Windows.Forms</code> GUI classes.

## Enabling the .NET Framework Interface

The .NET Framework interface is enabled when the DYALOG_NETCORE configuration parameter is set to `0`; this is the default setting on Microsoft Windows (a setting of `1` enables the .NET interface).

!!! Info "Information"
    The .NET Framework interface and .NET interface cannot be enabled simultaneously.

For information on how to set configuration parameters, see the _Dyalog for Microsoft Windows Installation and Configuration Guide_. To check the value of DYALOG_NETCORE, enter the following  when in a Session:
```apl
+2⎕NQ'.' 'GetEnvironment' 'DYALOG_NETCORE'
```

# Verifying the Installation

If the interpreter cannot locate the .NET code, then an error message is generated when attempting the following:
```apl
      ⎕USING←'System'
      DateTime.Now
VALUE ERROR: Undefined name: DateTime
      DateTime.Now

```

In this situation, ensure that the .NET Framework has been installed according to [Microsoft's .NET documentation](https://docs.microsoft.com/en-gb/dotnet/) and the .NET Framework interface has been enabled by setting DOTNET_NETCORE to `0` (see [Verifying the Installation](#verifying)).

If everything has been installed and enabled correctly, then the version of .NET Framework in use will be returned by the following statement:
```apl
      ⎕USING←'System' ⋄ Environment.Version
```
	
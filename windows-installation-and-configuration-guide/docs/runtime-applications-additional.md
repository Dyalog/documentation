<h1 class="heading"><span class="name">Run-Time Applications Additional Considerations</span></h1>

## Accessing your Application using Ride

If you wish to access your run-time application remotely using Ride, you must  put a copy of the appropriate Conga DLLs (see [Files](files-and-directories.md)) in the same directory as your .EXE or workspace.

## Additional Files for SQAPL

If your application uses the *SQAPL/EL ODBC* interface, you must distribute and install four additional components.

- SQAPL INI
- SQAPL ERR
- SQAPL DLL
- APLUNICD INI

For the names of the files corresponding to these components, see [Files](files-and-directories.md).

The SQAPL DLL must be installed in the user's Windows directory or be on the user's path.

## Miscellaneous Other Files

### DyaRes DLL

If your run-time application uses any of the bitmaps or other GUI resources that are built into the Dyalog Session, you must include the DyaRes DLL with your application.

### AUXILIARY PROCESSORS

If you use any of the Auxiliary Processors (APs) included in the sub-directory `xutils`, you must include these with your application. Note that, like workspaces, Dyalog APL searches for APs using the **WSPATH** parameter. If your application uses APs, you must ensure that you specify **WSPATH** or that the default **WSPATH** is adequate for your application..

### DYALOG32 and/or DYALOG64

This DLL is used by some of the functions provided in the `QUADNA.DWS` workspace. If you include any of these in your application this DLL must be installed in the user's Windows directory or be on the user's path.

## Universal C Runtime DLLs

Under Windows, many of the Dyalog APL run-time components (.EXE and .DLL) are linked dynamically with the Microsoft Universal C Runtime library (the UCRT) which is supplied and installed as part of the normal Dyalog development installation.

At execution time it is important that the Dyalog runtime components bind with a version of the UCRT that is compatible with (that is, the same as or newer than) the one with which they were built.

### Windows 10

If the end-user of the Dyalog application is known to be running Windows 10, the Dyalog application will pick up the system-wide UCRT which is part of Windows 10. There is therefore no need to include the UCRT with a Dyalog run-time application.

### Other Versions of Windows

The UCRT is not supplied with versions of Windows prior to Windows 10. On these platforms, it is therefore necessary to install the UCRT as part of the installation of the Dyalog run-time application. There are two ways to achieve this which are referred to herein as the VCRedist installation and App-local installation. Dyalog recommends the former.

#### VCRedist Installation (Recommended)

The VCRedist package, which includes the UCRT, is supplied with the Dyalog development package.

Simply copy the `vc_redistx86.exe` (32-bit version) or `vc_redistx64.exe` (64-bit version) program from the Dyalog development package into your own installation package and  execute it as part of the installation of your Dyalog run-time application. This installs the UCRT into a shared Windows location; in effect the UCRT becomes part of the Windows system. The installation therefore requires Administrator privileges.

#### App-local Installation

An alternative is to install the UCRT components into the same directory as your Dyalog run-time application. There are two ways to obtain these files.

### Either

Install the Dyalog development package (ideally onto a separate system just for this purpose) without administrator rights. This will perform an App-local installation of Dyalog itself. Then copy the UCRT files into your installation package. These files are:

- those beginning with `api-ms*`
- `ucrtbase.dll`
- `vcruntime140.dll`

### Or

Download and install the Windows 10 SDK from: [https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk](https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk), and follow the instructions in the link below. [https://blogs.msdn.microsoft.com/vcblog/2015/03/03/introducing-the-universal-crt](https://blogs.msdn.microsoft.com/vcblog/2015/03/03/introducing-the-universal-crt)

Finally, modify your installer to add these files to the same folder as your Dyalog run-time application.

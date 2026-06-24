# Introduction
	
This document describes the requirements for installing Dyalog v21.0 and the functionality changes in Dyalog v21.0 compared with Dyalog v20.0.

!!! Info "Information"  
    If you are upgrading from Dyalog v19.0 or earlier to Dyalog v21.0, you are advised to read the Release Notes for any intermediate versions in conjunction with this document.
	
## Release Highlights

Key enhancements in Dyalog v21.0 include the following:

- `⎕DT` has been extended to validate and parse text-format datetimes. It now also includes formatting features prototyped as `1200⌶`.
- `⎕SYSTEM` provides information about Dyalog and the environment, including the operating system, important library versions, and the current/initial/temporary directories.
- .NET generics are now fully supported for both .NET and .NET Framework, enabling the creation and instantiation of concrete versions of generic classes and calling of generic methods.
- A complete Software Bill of Materials is now included, making it easier to document files that are included when redistributing solutions built on Dyalog.

For more information on these and other changes introduced in Dyalog v21.0, see [New and Enhanced Features](new-enhanced.md).
	
## Tools
	
Some of the tools that are supplied with Dyalog or can be downloaded separately have independent version numbers; new versions of some of these tools are released in parallel with new versions of the interpreter. For Dyalog v21.0, these include:

- Conga v3.7
- HTTPCommand v5.11
    - GitHub repository – [https://github.com/Dyalog/HttpCommand](https://github.com/Dyalog/HttpCommand/)
	- Documentation – [https://dyalog.github.io/HttpCommand/5.11](https://dyalog.github.io/HttpCommand/5.11/)
- Link v4.2
    - GitHub repository – [https://github.com/Dyalog/link](https://github.com/Dyalog/link/)
	- Documentation – [https://dyalog.github.io/link/4.2](https://dyalog.github.io/link/4.2/)
- Ride v4.6
    - GitHub repository – [https://github.com/Dyalog/ride](https://github.com/Dyalog/ride/)
	- Documentation – [https://dyalog.github.io/ride/4.6](https://dyalog.github.io/ride/4.6/)
- SALT v2.9
- SQAPL v6.7
- User Commands v2.8


Changes to tools are not included within these Release Notes.

!!! Info "Information"
     It is not necessary to keep tool versions synchronised with the interpreter version, but doing so will provide the optimal experience.

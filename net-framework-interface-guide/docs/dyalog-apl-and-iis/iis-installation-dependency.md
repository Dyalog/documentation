<h1 class="heading"><span class="name">IIS Installation Dependency</span></h1>

During installation, Dyalog registers itself with ASP.NET as an ASP.NET programming language. Among other things, this allows ASP.NET web pages to be written in Dyalog. The Dyalog installation program  also registers the Dyalog asp.net sample applications as IIS *Virtual Directories*.

It is not practical for the Dyalog `setup.exe` to perform these tasks unless IIS and ASP.NET are already installed. Furthermore, unless IIS and ASP.NET are already installed and activated on the system, the Dyalog sub-directory `Samples/asp.net` will not even be copied onto the system, because the samples it contains would be inoperable.

If IIS is installed after Dyalog, it is necessary to de-install and then re-install Dyalog to enable the registration of Dyalog as an ASP.NET Programming language to occur, and for the `Samples/asp.net` sub-directory to be copied onto the system and the samples registered as IIS Virtual Directories.

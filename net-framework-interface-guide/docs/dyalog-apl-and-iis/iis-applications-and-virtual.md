<h1 class="heading"><span class="name">IIS Applications, Virtual Directories, Application Pools</span></h1>

IIS supports the concept of an *Application*. An application is a logically separate service or web site. IIS can run any number of Applications concurrently. The files associated with an application are stored in a physical directory on disk, which is linked to an IIS *Virtual Directory*. The name of the Virtual Directory is the name of the Application or Web Site.

The Dyalog APL distribution contains a directory named `Dyalog\Samples\asp.net` and a set of sub-directories each of which contains a sample application.

During the installation of Dyalog APL, these are automatically registered as IIS Virtual Directories, under a common root. The name of the root begins  `dyalog.net` followed by the Dyalog Version number, the edition (Unicode or classic), and the architecture (32-bit or 64-bit). For example, `dyalog.net.15.0.unicode.64` [^1]. The name of the root application is referred to henceforth as `dyalog.net`.

IIS applications run in application pools. An application pool is a group of one or more URLs that are served by the same worker process or set of worker processes which are separate from the worker process that services another application pool. This mechanism isolates applications from one another, providing resilience should any one application fail.

Each `dyalog.net` application is associated with an application pool named Dyalog APL xx (.NET v4.0 Classic[^2]), where xx is 32 or 64) which is created if required during installation.

When you want to run the Web Services and Web Page examples, you do so by specifying the URL `http://localhost/dyalog.net.xxxx/`

These samples can be easily found by selecting the *Documentation Centre* menu item from the Help menu on the Dyalog session, and scrolling down to the Tutorials section.

[^1]: Versions of Dyalog APL prior to Version 11.0 created Virtual Directories under apl.net .
[^2]: The term NET v4.0 Classic refers to the name of a standard application pool on which it is based, and has nothing to do with the Classic variant of Dyalog.

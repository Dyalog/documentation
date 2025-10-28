<h1 class="heading"><span class="name">Global.asax, Application and Session Objects</span></h1>

When a Web Service runs, it has access to the Application and Session objects. These are objects provided by ASP.NET through which you can manage the execution of the Web Service. ASP.NET creates an Application object when it first starts the Application, that is, when any client requests any Web Service or Web Page stored in the same IIS Virtual Directory. It also creates a Session object for each client process.

When the first request comes in for an ASP.NET application, ASP.NET checks for an optional file named `global.asax`, and if it is there it compiles it. The application's `global.asax` instance is then used to apply application events.

`global.asax` typically defines callback functions to be executed on the various `Application` and `Session` events, such as `Application_Start`, `Application_End`, `Session_Start`, `Session_End` and so forth.

Dyalog allows you to use APL functions in the `global.asax` script. This allows you to initialise your APL application when it is first invoked, and to close it down cleanly when it is terminated.

For example, you can use `global.asax` to tie a component file on start-up, and untie it on termination.

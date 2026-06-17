<h1 class="heading"><span class="name">Global.asax, and Application and Session Objects</span></h1>

When a web service runs, it has access to the application and session objects. These are objects provided by ASP.NET through which you can manage the execution of the web service. ASP.NET creates an application object when it first starts the application, that is, when any client requests any web service or web page stored in the same IIS virtual directory. It also creates a session object for each client process.

When the first request comes in for an ASP.NET application, ASP.NET checks for an optional file called **global.asax**; if it exists, then it compiles it. The application's **global.asax** instance is then used to apply application events.

**global.asax** typically defines callback functions to be executed on the various <code class="language-nonAPL">Application</code> and <code class="language-nonAPL">Session</code> events, such as <code class="language-nonAPL">Application_Start</code>, <code class="language-nonAPL">Application_End</code>, <code class="language-nonAPL">Session_Start</code>, <code class="language-nonAPL">Session_End</code> and so on.

Dyalog allows you to use APL functions in the **global.asax** script. This allows you to initialise your APL application when it is first invoked, and to close it down cleanly when it is terminated. For example, you can use **global.asax** to tie a component file on start-up, and untie it on termination.

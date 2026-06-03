<h1 class="heading"><span class="name">Writing Web Services</span></h1>

A web service can be thought of as a Remote Procedure Call. However, it is a remote procedure call that can be made over the Internet using character-based messages.

Web services are implemented using Simple Object Access Protocol (SOAP), Extensible Mark-up Language (XML) and Hypertext Transfer Protocol (HTTP). Web services do not require proprietary network protocols or software. Web service calls and responses can successfully be transmitted over the Internet without the need to specially configure firewalls.

A web service is a class that can be called by any program running on the computer, any program running on a computer on the same LAN, or any program running on any computer on the internet.

Web services are hosted (that is, executed) by ASP.NET running under Microsoft IIS. Each web service sits on a single server computer and runs there under ASP.NET/IIS. The messages that invoke the web service, pass its arguments, and return its results, utilise standard HTTP/SOAP/XML protocols.

A web service consists of a single text script file, with the extension **.asmx**, in an IIS virtual directory on the server computer.

A web service can expose a number of _methods_ and _properties_. Methods can be called _synchronously_ (the calling process waits for the result) or _asynchronously_ (the calling process invokes the method, continues, and subsequently checks for the result of the previous call).

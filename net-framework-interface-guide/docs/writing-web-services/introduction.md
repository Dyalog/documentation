<h1 class="heading"><span class="name">Introduction</span></h1>

A Web Service can be thought of as a Remote Procedure Call. However, it is a remote procedure call that can be made over the Internet using character-based messages.

Web Services are implemented using Simple Object Access Protocol (SOAP), Extensible Mark-up Language (XML) and Hypertext Transfer Protocol (HTTP). Web Services do not require proprietary network protocols or software. Web Service calls and responses can successfully be transmitted over the Internet without the need to specially configure firewalls.

A Web Service is a class that may be called by any program running on the computer, any program running on a computer on the same LAN, or any program running on any computer on the internet.

Web Services are hosted (that is, executed) by ASP.NET running under Microsoft IIS. Any one Web Service sits on a single server computer and runs there under ASP.NET/IIS. The messages that invoke the Web Service, pass its arguments, and return its results, utilise standard HTTP/SOAP/XML protocols.

A Web Service consists of a single text script file, with the extension `.asmx`, in an IIS Virtual Directory on the server computer.

A Web Service may expose a number of Methods and Properties. Methods may be called *synchronously* (the calling process waits for the result) or *asynchronously* (the calling process invokes the method, continues for a bit, and then subsequently checks for the result of the previous call).

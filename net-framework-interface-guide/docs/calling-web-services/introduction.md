<h1 class="heading"><span class="name">Introduction</span></h1>

In order to call a Web Service, you need a "proxy class" on the client, which exposes the same methods and properties as the web service. The proxy creates the illusion that the web service is present on the client. Client applications create instances of the proxy class, which in turn communicate with the Web Service via IIS, using TCP/IP and HTTP/XML protocols.

Microsoft provides a utility called `WSDL.EXE` that queries the metadata (Web Service Definition Language) of a Web Service and generate C# source code for a matching proxy class.

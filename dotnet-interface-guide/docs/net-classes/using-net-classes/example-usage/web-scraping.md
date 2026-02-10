# Web Scraping

.NET provides a range of classes for accessing the internet from a program. This section works through an example that shows how to read the contents of a web page. It is complicated, but realistic (for example, it includes code to cater for a firewall/proxy connection to the internet). It is only 9 lines of APL code, but each line requires careful explanation.

Start by defining `⎕USING` so that it specifies all of the necessary .NET namespaces and assemblies:
```apl
      ⎕USING←,⊂'System,System.dll'
      ⎕USING,←⊂'System.Net, System.Net.Requests'
      ⎕USING,←⊂'System.IO'
```

The WebRequest class in the System.Net  .NET namespace implements .NET's request/response model for accessing data from the internet. For this example, a WebRequest object needs to be associated with the URI `http://www.dyalog.com` (WebRequest is an example of a static class – its methods can be used without creating instances of it):
```apl
      wrq←WebRequest.Create ⊂'http://www.dyalog.com'
```

Potentially confusingly, if the URI specifies a protocol of "http://" or "https://", an object of type HttpWebRequest is returned rather than a simple WebRequest. The effect of this is that, at this stage, wrq is an HttpWebRequest object.
```apl
      wrq
System.Net.HttpWebRequest
```

The HttpRequest class has a GetResponse method that returns a response from an internet resource. Although it is not yet HTML, the result is an object of type System.Net.HttpWebResponse:
```apl
      wr←wrq.GetResponse
      wr
System.Net.HttpWebResponse
```

The HttpWebResponse class has a GetResponseStream method whose result is of type System.Net.ConnectStream. This object, whose base class is System.IO.Stream, provides methods to read and write data both synchronously and asynchronously from a data source, which in this case is physically connected to a TCP/IP socket:
```apl
      str←wr.GetResponseStream
      str
System.Net.Http.HttpConnection+ChunkedEncodingReadStream
```

However, the Stream class is designed for byte input and output; what is needed in this example is a class that reads characters in a byte stream using a particular encoding. This is a job for the System.IO.StreamReader class. Given a Stream object, create a new instance of a StreamReader by passing it the Stream as a parameter:
```apl
      rdr←⎕NEW StreamReader str
      rdr
System.IO.StreamReader
```

Finally, use the ReadToEnd method of the StreamReader to get the contents of the page:
```apl
      s←rdr.ReadToEnd
      ⍴s
20295
```

To avoid running out of connections, it is necessary to close the stream:
```apl
      str.Close
			 
```

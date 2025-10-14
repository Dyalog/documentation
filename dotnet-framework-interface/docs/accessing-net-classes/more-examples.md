<h1 class="heading"><span class="name">More Examples</span></h1>

## Directory and File Manipulation

The .NET Namespace `System.IO` (also in the Assembly `mscorlib.dll`) provides some useful facilities for manipulating files. For example, you can create a `DirectoryInfo` object associated with a particular directory on your computer, call its `GetFiles` method to obtain a list of files, and then get their `Name` and `CreationTime` properties.
```apl
      ⎕USING←,⊂'System.IO'
      d←⎕NEW DirectoryInfo (⊂'C:\Dyalog')
```

`d` is an instance of the `Directory` Class, corresponding to the directory `c:\Dyalog`[^1].
```apl
      d
C:\Dyalog
```

The `GetFiles` method returns a list of files; actually, `FileInfo` objects, that represent each of the files in the directory: Its optional argument specifies a filter; for example:
```apl
      d.GetFiles ⊂'*.exe'
 evalstub.exe  exestub.exe  dyalog.exe  dyalogrt.exe
```

The `Name` property returns the name of the file associated with the `File` object:
```apl
      (d.GetFiles ⊂'*.exe').Name
 evalstub.exe  exestub.exe  dyalog.exe  dyalogrt.exe
```

And the `CreationTime` property returns its creation time, which is a `DateTime` object:
```apl
      (d.GetFiles ⊂'*.exe').CreationTime
```

01/04/2004 09:37:01  01/04/2004 09:37:01  08/06/2004 ...

If you call `GetFiles` without an argument (in APL, with an argument of `⍬`), it returns a complete list of files:
```apl
      files←d.GetFiles ⍬
```

Taking advantage of namespace reference array expansion, an expression to display file names and their creation times is as follows.
```apl
      files,[1.5]files.CreationTime
 relnotes.hlp       03/02/2004 11:47:02 
 relnotes.cnt       03/02/2004 11:47:02 
 def_uk.dse         22/03/2004 12:13:31 
 DIALOGS.HLP        22/03/2004 12:13:31 
 dyares32.dll       22/03/2004 12:13:40 
 ...
```

## Sending an email

The .NET Namespace `System.Web.Mail` provides objects for handing email.

You can create a new email message as an instance of the `MailMessage` class, set its various properties, and then send it using the `SmtpMail` class.

Please note that these examples will only work if your computer is configured to allow you to send email in this way.
```apl
      ⎕USING←'System.Web.Mail,System.Web.dll'
      m←⎕NEW MailMessage
      m.From←'tony.blair@uk.gov'
      m.To←'sales@dyalog.com'
      m.Subject←'order'
      m.Body←'Send me 100 copies of Dyalog now'
 
      SmtpMail.Send m
```

However, note that the `Send` method of the `SmtpMail` object is overloaded and may be called with a single parameter of type `System.Web.Mail.MailMessage` as above, or four parameters of type `System.String`:

So instead, you can just say:
```apl
      SmtpMail.Send 'tony.blair@uk.gov'
                    'sales@dyalog.com'
                    'order'
                    'Send me the goods'
 
```

## Web Scraping

The .NET Framework provides a whole range of classes for accessing the internet from a program. The following example illustrates how you can read the contents of a web page. It is complicated, but realistic, in that it includes code to cater for a firewall/proxy connection to the internet. It is only 9 lines of APL code, but each line requires careful explanation.

First we need to define `⎕USING` so that it specifies all of the .NET Namespaces and Assemblies that we require.
```apl
      ⎕USING←'System,System.dll' 'System.Net' 'System.IO'
```

The `WebRequest` class in the .NET Namespace `System.Net` implements the .NET Framework's request/response model for accessing data from the Internet. In this example we create a `WebRequest` object associated with the URI `https://www.example.com`. Note that `WebRequest` is an example of a static class. You don't make instances of it; you just use its methods.
```apl
      wrq←WebRequest.Create ⊂'https://www.example.com'
```

In fact (and somewhat confusingly) if the URI specifies a scheme of "http://" or "https://", you get back an object of type `HttpWebRequest` rather than a plain and simple `WebRequest`. So, at this stage, `wrq` is an `HttpWebRequest` object.
```apl
      wrq
System.Net.HttpWebRequest
```

This class has a `Proxy` property through which you specify the proxy information for a request made through a firewall. The value assigned to the `Proxy` property has to be an object of type `System.Net.WebProxy`. So first we must create a new `WebProxy` object specifying the hostname and port number for the firewall. You will need to change this statement to suit your own internet configuration (it may even not be necessary to do this).
```apl
      PX←⎕NEW WebProxy(⊂'http://dyagate.dyadic.com:8080')
      PX
System.Net.WebProxy
```

Having set up the `WebProxy` object as required, we then assign it to the `Proxy` property of the `HttpRequest` object `wrq`.
```apl
      wrq.Proxy←PX
```

The `HttpRequest` class has a `GetResponse` method that returns a response from an internet resource. No it's not HTML (yet), the result is an object of type `System.Net.HttpWebResponse`.
```apl
      wr←wrq.GetResponse
      wr
System.Net.HttpWebResponse
```

The `HttpWebResponse` class has a `GetResponseStream` method whose result is of type `System.Net.ConnectStream`. This object, whose base class is `System.IO.Stream`, provides methods to read and write data both synchronously and asynchronously from a data source, which in this case is physically connected to a TCP/IP socket.
```apl
      str←wr.GetResponseStream
      str
System.Net.ConnectStream
```

However, there is yet another step to consider. The `Stream` class is designed for byte input and output; what we need is a class that reads characters in a byte stream using a particular encoding. This is a job for the `System.IO.StreamReader` class. Given a `Stream` object, you can create a new instance of a `StreamReader` by passing it the `Stream` as a parameter.
```apl
      rdr←⎕NEW StreamReader str
      rdr
System.IO.StreamReader
```

Finally, we can use the `ReadToEnd` method of the `StreamReader` to get the contents of the page.
```apl
      s←rdr.ReadToEnd
      ⍴s
45242
```

Note that to avoid running out of connections, it is necessary to close the Stream:
```apl
      str.Close
 
```

[^1]: In this document, we will refer to the location where Dyalog is installed as C:\Dyalog. Your installation of Dyalog might be in a different folder or even on a different drive but the examples should work just the same it you replace C:\Dyalog by your folder name

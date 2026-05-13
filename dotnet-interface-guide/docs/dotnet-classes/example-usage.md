<h1 class="heading"><span class="name">Example Usage</span></h1>

## Directory and File Manipulation

The .NET namespace <code class="language-nonAPL">System.IO</code> (in the <code class="language-nonAPL">System.IO.FileSystem</code> assembly) provides some useful facilities for manipulating files. For example, you can create a <code class="language-nonAPL">DirectoryInfo</code> object associated with a particular directory on your computer, call its <code class="language-nonAPL">GetFiles</code> method to obtain a list of files, and then get their <code class="language-nonAPL">Name</code> and <code class="language-nonAPL">CreationTime</code> properties:
```apl
      ⎕USING←,⊂'System.IO, System.IO.FileSystem'
      dir←'C:\Program Files\Dyalog\Dyalog APL-64 19.0 Unicode'
      d←⎕NEW DirectoryInfo (⊂dir)
```

where `d` is an instance of the <code class="language-nonAPL">Directory</code> class, corresponding to the directory **[DYALOG]**.

!!! Info "Information"
    **[DYALOG]** refers to the directory in which Dyalog is installed; this example assumes **[DYALOG]** to be **C:/Program Files/Dyalog/Dyalog APL-64 19.0 Unicode**.

The <code class="language-nonAPL">GetFiles</code> method returns a list of files (more precisely, <code class="language-nonAPL">FileInfo</code> objects) that represent each of the files in the directory. Its optional argument specifies a filter. For example:
```apl
      d.GetFiles ⊂'*.exe'
C:\Program Files\Dyalog\Dyalog APL-64 19.0 Unicode\dyaedit.exe  
C:\Program Files\Dyalog\Dyalog APL-64 19.0 Unicode\dyalog.exe  
C:\Program Files\Dyalog\Dyalog APL-64 19.0 Unicode\dyalogc.exe  
C:\Program Files\Dyalog\Dyalog APL-64 19.0 Unicode\dyalogc64_unicode.exe  
C:\Program Files\Dyalog\Dyalog APL-64 19.0 Unicode\dyalogrt.exe
  C:\Program Files\Dyalog\Dyalog APL-64 19.0 Unicode\dyascript.exe
```

The <code class="language-nonAPL">Name</code> property returns the name of the file associated with the <code class="language-nonAPL">File</code> object:
```apl
      (d.GetFiles ⊂'*.exe').Name
dyaedit.exe  dyalog.exe  dyalogc.exe  dyalogc64_unicode.exe  dyalogrt.exe  dyascript.exe
```

and the <code class="language-nonAPL">CreationTime</code> property returns its creation time, which is a <code class="language-nonAPL">DateTime</code> object:
```apl
     (d.GetFiles ⊂'*.exe').CreationTime
 08/02/2024 20:51:24  08/02/2024 20:50:06  08/02/2024 ...
```

Calling the <code class="language-nonAPL">GetFiles</code> overload that does not take any arguments (from Dyalog by supplying an argument of [`⍬`](../../../language-reference-guide/other-syntax/zilde/)) returns a complete list of files:
```apl
      files←d.GetFiles ⍬
      files
C:\Program Files\Dyalog\Dyalog APL-64 19.0 Unicode\aplunicd.ini...
```

Taking advantage of namespace reference array expansion, an expression to display file names and their creation times is:
```apl
      files,[1.5]files.CreationTime
C:\...\...Unicode\aplunicd.ini               08/02/2024 20:12:02  
C:\...\...Unicode\bridge190-64_unicode.dll   08/02/2024 20:47:36  
...
```

## Sending an Email

The .NET namespace <code class="language-nonAPL">System.Net.Mail</code> provides objects for handing email. You can create a new email message as an instance of the <code class="language-nonAPL">MailMessage</code> class, set its various properties and then send it using the <code class="language-nonAPL">SmtpClient</code> class.

<h4 class="example">Example</h4>

This example will only work if your computer is configured to allow you to send email.
```apl
∇ recip Send(subject msg);⎕USING;from;mail;to;builder;client;
                                      FROM_ADDRESS; EMAIL_SERVER
  ⎕USING←'System.Net.Mail,System.Net.Mail'

  FROM_ADDRESS←'someone@somewhere.com'
  EMAIL_SERVER←'mail.somwhere.com'

  from←⎕NEW MailAddress(⊂FROM_ADDRESS)
  to←⎕NEW MailAddress(recip '')
  mail←⎕NEW MailMessage (from to)
  mail.Body←msg
  mail.Subject←subject
  client←⎕NEW SmtpClient (⊂EMAIL_SERVER)
  client.Send mail
∇
```

This could then be called as follows:
```apl
'prime.minister@gov.uk' Send ('subject' ('line1' 'line2'))
```

## Web Scraping

.NET provides a range of classes for accessing the internet from a program. This section works through an example that shows how to read the contents of a web page. It is complicated, but realistic (for example, it includes code to cater for a firewall/proxy connection to the internet). It is only 9 lines of APL code, but each line requires careful explanation.

Start by defining [`⎕USING`](../../../language-reference-guide/system-functions/using/) so that it specifies all of the necessary .NET namespaces and assemblies:
```apl
      ⎕USING←,⊂'System,System.dll'
      ⎕USING,←⊂'System.Net, System.Net.Requests'
      ⎕USING,←⊂'System.IO'
```

The <code class="language-nonAPL">WebRequest</code> class in the <code class="language-nonAPL">System.Net</code> .NET namespace implements .NET's request/response model for accessing data from the internet. For this example, a WebRequest object needs to be associated with the URI `http://www.dyalog.com` (<code class="language-nonAPL">WebRequest</code> is an example of a static class – its methods can be used without creating instances of it):
```apl
      wrq←WebRequest.Create ⊂'http://www.dyalog.com'
```

Potentially confusingly, if the URI specifies a protocol of "http://" or "https://", an object of type <code class="language-nonAPL">HttpWebRequest</code> is returned rather than a simple WebRequest. The effect of this is that, at this stage, <code class="language-nonAPL">wrq</code> is an <code class="language-nonAPL">HttpWebRequest</code> object.
```apl
      wrq
System.Net.HttpWebRequest
```

The <code class="language-nonAPL">HttpRequest</code> class has a <code class="language-nonAPL">GetResponse</code> method that returns a response from an internet resource. Although it is not yet HTML, the result is an object of type <code class="language-nonAPL">System.Net.HttpWebResponse</code>:
```apl
      wr←wrq.GetResponse
      wr
System.Net.HttpWebResponse
```

The <code class="language-nonAPL">HttpWebResponse</code> class has a <code class="language-nonAPL">GetResponseStream</code> method whose result is of type <code class="language-nonAPL">System.Net.ConnectStream</code>. This object, whose base class is <code class="language-nonAPL">System.IO.Stream</code>, provides methods to read and write data both synchronously and asynchronously from a data source, which in this case is physically connected to a TCP/IP socket:
```apl
      str←wr.GetResponseStream
      str
System.Net.Http.HttpConnection+ChunkedEncodingReadStream
```

However, the <code class="language-nonAPL">Stream</code> class is designed for byte input and output; what is needed in this example is a class that reads characters in a byte stream using a particular encoding. This is a job for the <code class="language-nonAPL">System.IO.StreamReader</code> class. Given a <code class="language-nonAPL">Stream</code> object, create a new instance of a <code class="language-nonAPL">StreamReader</code> by passing it the <code class="language-nonAPL">Stream</code> as a parameter:
```apl
      rdr←⎕NEW StreamReader str
      rdr
System.IO.StreamReader
```

Finally, use the <code class="language-nonAPL">ReadToEnd</code> method of the <code class="language-nonAPL"></code> to get the contents of the page:
```apl
      s←rdr.ReadToEnd
      ⍴s
20295
```

!!! Info "Information"
    To avoid running out of connections, it is necessary to close the stream:  
    ```apl
          str.Close		 
    ```

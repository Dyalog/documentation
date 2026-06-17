<h1 class="heading"><span class="name">Example Usage</span></h1>

## Directory and File Manipulation

The .NET Namespace <code class="language-nonAPL">System.IO</code> (in the <code class="language-nonAPL">mscorlib</code> assembly) provides some useful facilities for manipulating files. For example, you can create a <code class="language-nonAPL">DirectoryInfo</code> object associated with a particular directory on your computer, call its <code class="language-nonAPL">GetFiles</code> method to obtain a list of files, and then get their <code class="language-nonAPL">Name</code> and <code class="language-nonAPL">CreationTime</code> properties:
```apl
      ⎕USING←,⊂'System.IO'
      d←⎕NEW DirectoryInfo (⊂'C:\Dyalog')
```

where `d` is an instance of the <code class="language-nonAPL">Directory</code> class, corresponding to the directory **[DYALOG]**.

!!! Info "Information"
    **[DYALOG]** refers to the directory in which Dyalog is installed; this example assumes **[DYALOG]** to be **C:\Dyalog**.

The <code class="language-nonAPL">GetFiles</code> method returns a list of files (more precisely, <code class="language-nonAPL">FileInfo</code> objects) that represent each of the files in the directory. Its optional argument specifies a filter. For example:
```apl
      d.GetFiles ⊂'*.exe'
evalstub.exe	exestub.exe	dyalog.exe	dyalogrt.exe

```

The <code class="language-nonAPL">Name</code> property returns the name of the file associated with the <code class="language-nonAPL">File</code> object:
```apl
      (d.GetFiles ⊂'*.exe').Name
evalstub.exe	exestub.exe	dyalog.exe	dyalogrt.exe
```

and the <code class="language-nonAPL">CreationTime</code> property returns its creation time, which is a <code class="language-nonAPL">DateTime</code> object:
```apl
     (d.GetFiles ⊂'*.exe').CreationTime
 05/03/2020 10:23:40  05/03/2020 10:23:28  14/11/2019 ...
```

Calling the <code class="language-nonAPL">GetFiles</code> overload that does not take any arguments (from Dyalog by supplying an argument of `⍬`) returns a complete list of files:
```apl
      files←d.GetFiles ⍬

```

Taking advantage of namespace reference array expansion, an expression to display file names and their creation times is:
```apl
      files,[1.5]files.CreationTime
relnotes.hlp	03/02/2004	11:47:02
relnotes.cnt	03/02/2004	11:47:02
def_uk.dse	22/03/2004	12:13:31
DIALOGS.HLP	22/03/2004	12:13:31
dyares32.dll	22/03/2004	12:13:40
...
```

## Sending an Email

The .NET namespace <code class="language-nonAPL">System.Web.Mail</code> provides objects for handing email. You can create a new email message as an instance of the <code class="language-nonAPL">MailMessage</code> class, set its various properties and then send it using the <code class="language-nonAPL">SmtpMail</code> class.

<h4 class="example">Example</h4>

This example will only work if your computer is configured to allow you to send email in this way.
```apl
      ⎕USING←'System.Web.Mail,System.Web.dll'
      m←⎕NEW MailMessage
      m.From←'tony.blair@uk.gov'
      m.To←'sales@dyalog.com'
      m.Subject←'order'
      m.Body←'Send me 100 copies of Dyalog APL now'
      SmtpMail.Send m
```

However, the <code class="language-nonAPL">Send</code> method of the <code class="language-nonAPL">SmtpMail</code> object is overloaded; it could be called with a single parameter of type <code class="language-nonAPL">System.Web.Mail.MailMessage</code> as above, or four parameters of type <code class="language-nonAPL">System.String</code>. An alternative is:
```apl
      SmtpMail.Send 'tony.blair@uk.gov'
                    'sales@dyalog.com'
                    'order'
                    'Send me the goods'
```

For more information on overloading, see [Overload Constructors](../advanced-techniques/#overloaded-constructors).

## Web Scraping

The .NET Framework provides a range of classes for accessing the internet from a program. This section works through an example that shows how to read the contents of a web page. It is complicated, but realistic (for example, it includes code to cater for a firewall/proxy connection to the internet). It is only 9 lines of APL code, but each line requires careful explanation.

Start by defining `⎕USING` so that it specifies all of the necessary .NET namespaces and assemblies:
```apl
      ⎕USING←'System,System.dll' 'System.Net' 'System.IO'
```

The <code class="language-nonAPL">WebRequest</code> class in the <code class="language-nonAPL">System.Net</code> .NET namespace implements the .NET Framework's request/response model for accessing data from the internet. For this example, a <code class="language-nonAPL">WebRequest</code> object needs to be associated with the URI `http://www.dyalog.com` (<code class="language-nonAPL">WebRequest</code> is an example of a static class – its methods can be used without creating instances of it):
```apl
      wrq←WebRequest.Create ⊂'http://www.dyalog.com'
```

Potentially confusingly, if the URI specifies a protocol of "http://" or "https://", an object of type <code class="language-nonAPL">HttpWebRequest</code> is returned rather than a simple <code class="language-nonAPL">WebRequest</code>. The effect of this is that, at this stage, <code class="language-nonAPL">wrq</code> is an <code class="language-nonAPL">HttpWebRequest</code> object.
```apl
      wrq
System.Net.HttpWebRequest
```

This class has a <code class="language-nonAPL">Proxy</code> property through which the proxy information is specified for a request made through a firewall. The value assigned to the <code class="language-nonAPL">Proxy</code> property has to be an object of type <code class="language-nonAPL">System.Net.WebProxy</code>. It might, therefore, be necessary to create a new <code class="language-nonAPL">WebProxy</code> object specifying the hostname and port number for the firewall:
```apl
      PX←⎕NEW WebProxy(⊂'http://dyagate.dyadic.com:8080')
      PX
System.Net.WebProxy
```

(This statement will need to be amended to suit each internet configuration, and might not be required).

Having set up the <code class="language-nonAPL">WebProxy</code> object as required, the <code class="language-nonAPL">Proxy</code> property of the <code class="language-nonAPL">HttpRequest</code> object <code class="language-nonAPL">wrq</code> is then assigned to it:
```apl
      wrq.Proxy←PX
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
System.Net.ConnectStream
```

However, the <code class="language-nonAPL">Stream</code> class is designed for byte input and output; what is needed in this example is a class that reads characters in a byte stream using a particular encoding. This is a job for the <code class="language-nonAPL">System.IO.StreamReader</code> class. Given a <code class="language-nonAPL">Stream</code> object, create a new instance of a <code class="language-nonAPL">StreamReader</code> by passing it the <code class="language-nonAPL">Stream</code> as a parameter:
```apl
      rdr←⎕NEW StreamReader str
      rdr
System.IO.StreamReader
```

Use the <code class="language-nonAPL">ReadToEnd</code> method of the <code class="language-nonAPL">StreamReader</code> to get the contents of the page:
```apl
      s←rdr.ReadToEnd
      ⍴s
45242
```

Finally, to avoid running out of connections, it is necessary to close the stream:
```apl
      str.Close
```

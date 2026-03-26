# Sending an Email

The .NET namespace System.Net.Mail provides objects for handing email. You can create a new email message as an instance of the MailMessage class, set its various properties and then send it using the SmtpClient class.

Example

This example will only work if your computer is configured to allow you to send email.
```apl
∇ recip Send(subject msg);⎕USING;from;mail;to;builder;client;
                                      FROM_ADDRESS; EMAIL_SERVER
  ⎕USING←'System.Net.Mail,System.Net.Mail'
```
```apl

  FROM_ADDRESS←'someone@somewhere.com'
  EMAIL_SERVER←'mail.somwhere.com'
```
```apl

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

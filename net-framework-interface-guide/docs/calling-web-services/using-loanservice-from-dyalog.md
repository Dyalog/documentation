<h1 class="heading"><span class="name">Using LoanService from Dyalog APL</span></h1>

For example, the above call to `MakeProxy` will create a C# source code file called `LoanService.cs`, and an assembly called `LoanService.dll` in your current directory. The name of the proxy class in `LoanService.dll` is `LoanService`.

You use this proxy class in exactly the same way that you use any .NET class. For example:
```apl
      ⎕USING ←,⊂',.\LoanService.dll'
      LN←⎕NEW LoanService
      LN.CalcPayments 100000 20 10 15 2
LoanResult
```

Notice that, as expected, the result of `CalcPayments` is an object of type `LoanResult`. For convenience, we will assign this to `LR` and then reference its fields:
```apl
      LR←LN.CalcPayments 100000 20 10 15 2
      LR.Periods
10 11 12 13 14 15 16 17 18 19 20
      LR.InterestRates
2 2.5 3 3.5 4 4.5 5 5.5 6 6.5 7 7.5 8 8.5 9 9.5 10 10.5 ...
      LR.(((⍴InterestRates),⍴Periods)⍴Payments)
920.1345384 844.5907851 781.6836919 728.4970675 682.947 ...
```

The `Payments` field is, of course, a vector because it was defined that way. However, as can be seen above, it is easy to give it the "right" shape.

When you execute the `CalcPayments` method in the proxy class, the class transforms and packages up your arguments into an appropriate SOAP/XML stream and sends them, using TCP/IP, to the URL that represents the Web Service wherever that URL is on the internet or your Intranet. It then decodes the SOAP/XML that comes back, and returns the response as the result of the method.

Note that, depending upon the speed of your connection, and the logical distance away of the Web Service itself, calling a Web Service method can take a significant amount of time; regardless of how much time it actually takes to execute on its server.

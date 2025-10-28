<h1 class="heading"><span class="name">Asynchronous Use</span></h1>

Web Services provide both synchronous (client calls the function and waits for a result) and asynchronous operation.

Each method is exposed as a function with the same name (the synchronous version) together with a pair of functions with that name prefixed with `Begin` and `End` respectively.

The `Beginxxx` functions take two additional parameters; a delegate class that represents a callback function and a state parameter.

To initiate the call, you execute the `Beginxxx` method using the standard parameters followed by two objects. The first is an object of type `System.AsyncCallback` that represents an asynchronous callback, that is, a callback to be invoked when the asynchronous call is complete. The second is an object which is used to supply extra information. We will see how callbacks are used later in this section. If you are not using a callback, these items should be null object references. You can specify a reference to a null object using the expression `(⎕NS'')`. For example, using the `LoanService` sample as above:
```apl
      A←LN.BeginCalcPayments 10000 16 10 12
                             9(⎕NS'')(⎕NS'')
```

The result is an object of type `WebClientAsynchResult`.
```apl
      A
System.IAsyncResult ⎕CLASS System.Web.Services.Protocols.WebClientAsyncResult
```

Then, some time later, you call the `Endxxx` method with this object as a parameter. For example:
```apl
      LN.EndCalcPayments A
LoanResult
```

You can execute several asynchronous calls in parallel:
```apl
      A1←LN.BeginCalcPayments 20000 20 10 15
                              7(⎕NS'')(⎕NS'')
      A2←LN.BeginCalcPayments 30000 10  8 12
                              3(⎕NS'')(⎕NS'')
 
      LN.EndCalcPayments A1
LoanResult
      LN.EndCalcPayments A2
LoanResult
```

## Using a callback

The simple approach described above is not always practical. If it can take a significant amount of time for the web service to respond, you may prefer to have the system notify you, via a callback function, when the result from the method is available.

The example function `TestAsyncLoan` in the workspace `samples\asp.net\webservices\webservices.dws` illustrates how you can do this. It is somewhat artificial, but hopefully explains the mechanism that is involved.

`TestAsyncLoan` itself is just a convenience function that calls `AsyncLoan` with suitable arguments. `TestAsyncLoan` takes an argument of 1 or 0 that determines whether or not a Proxy class for `LoanService` is to be built.
```apl
     ∇ TestAsyncLoan MAKEPROXY
[1]    (⍕MAKEPROXY),' AsyncLoan 10000 10 8 5 3'
[2]    MAKEPROXY AsyncLoan 10000 10 8 5 3
     ∇
```

The `AsyncLoan` function and its callback function `GetLoanResult` are more interesting.
```apl
     ∇ {MAKEPROXY}AsyncLoan ARGS;DLL;SINK;LN;AS;AR
[1]    :If 2≠⎕NC'MAKEPROXY' ⋄ MAKEPROXY←0 ⋄ :EndIf
[2]    :If MAKEPROXY
[3]       DLL←MakeProxy'http://localhost/dyalog.net/loan/
                         loan.asmx'
[4]    :Else
[5]       DLL←'.\LoanService.dll'
[6]    :EndIf
[7]    ⎕USING←'System'(',',DLL)
[8]    LN←⎕NEW LoanService 
[9]    AS←⎕NEW System.AsyncCallback,⊂⎕OR'GetLoanResult'
[10]   AR←LN.BeginCalcPayments ARGS,AS,LN
[11]   'AsyncLoan waits for async call to complete'
[12]   :While 0=AR.IsCompleted
[13]       ⍞←'.'
[14]   :EndWhile
     ∇
     ∇ GetLoanResult arg;OBJ;LR;RSLT
[1]    'GetLoanResult callback fires ...'
[2]    OBJ←arg.AsyncState
[3]    LR←OBJ.EndCalcPayments arg
[4]    RSLT←LR.(((⍴Periods),(⍴InterestRates))⍴Payments)
[5]    RSLT←((⊂''),LR.Periods),(LR.InterestRates),[1]RSLT
[6]    'Result is'
[7]    ⎕←RSLT
     ∇
```

The effect of running `TestAsyncLoan` is as follows:
```apl
      TestAsyncLoan 0
0 AsyncLoan 10000 10 8 4 3
 
...AsyncLoan waits for async call to complete...
...GetLoanResult callback fires ...
 
...Result is
      3           3.5         4         
 8  117.2957193 105.7694035  96.5607447 
 9  119.5805173 108.0741442  98.88586746
121.892753  110.409689  101.2451382
```

`AsyncLoan[8]` creates a new instance of the `LoanService` class called `LN`. The next line creates an object of type `System.AsyncCallback` named `AS`. This object, which is termed a *delegate*, identifies the callback function that is to be invoked when the asynchronous call to `CalcPayments` is complete. In this case, the name of the callback function is `GetLoanResult`.  Note that `⎕OR` is necessary because the `AsyncCallback` constructor must be called with a parameter of type `System.Object`. The line `AsyncLoan[10]` calls `BeginCalcPayments` with the parameters for `CalcPayments`, followed by references to `AS` (which identifies the callback) and `LN`, which identifies the object in question. The latter will turn up in the argument supplied to the `GetLoanResult` callback. Lines[12-14] loop, displaying dots, until the asynchronous call is complete. `GetLoanResult` will be invoked during or immediately after this loop, and will be executed in a different APL thread.

When the `GetLoanResult` callback is invoked, its argument `arg` is an object of type `System.Web.Services.Protocols.WebClientAsyncResult`. It is in fact a reference to the same object `AR` that was the result returned by `BeginCalcPayments`.

This object has an `AsyncState` property that references the `LoanService` object `LN` that we passed as the final parameter to `BeginCalcPayments`. `GetLoanResult[2]` retrieves this object and assigns it to `OBJ`. `GetLoanResult[3]` calls the `EndCalcPayments` method, passing it `arg` as the `AsyncResult` parameter as before. The resulting `LoanResult` object is then formatted and displayed.

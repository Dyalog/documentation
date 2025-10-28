<h1 class="heading"><span class="name">Exploring Web Services</span></h1>

You can use the Workspace Explorer to browse the proxy class associated with a Web Service, in exactly the same way that you can browse any other .NET Assembly. The following screen shots show the *Metadata* for `LoanService`, loaded from the `LoanService.dll` proxy.

Remember, `LoanService` was written in `APLScript`, but it appears and behaves just like any other .NET class.

The first picture displays the structure of the `LoanResult` class.

![](../img/exploring-loanservice-1.png)

The second picture shows the methods exposed by `LoanService`. In addition to `CalcPayments`, which was written in `APLScript`, there are a large number of other methods, which have been inherited from the base class.

![](../img/exploring-loanservice-2.png)

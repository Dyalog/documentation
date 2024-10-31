




<h1 class="heading"><span class="name">Disposable Statement</span> <span class="command">:Disposable</span></h1>



[Formal Definition](disposable-statement-definition.md){: .noprint }


The Dyalog interface to .NET involves the creation and removal of .NET objects. Many such objects are *managed* in that the .NET Common Language RunTime (CLR)  automatically releases the memory allocated to the object when that object is no longer used. However, it is not possible to predict when the CLR garbage collection will occur. Furthermore, the garbage collector has no knowledge of *unmanaged* resources such as window handles, or open files and streams.



Typically, .NET classes implement a special interface called IDisposable which provides a standard way for applications to release memory and other resources when an instance is removed. Furthermore, the C# language has the using keyword, which "Provides a convenient syntax that ensures the correct use of IDisposable objects."


The `:Disposable array` statement in Dyalog APL provides a similar facility to C#'s using. `array` may be a scalar or vector of namespace references.


When the block is exited, any .NET objects in `array` that implement IDisposable will have IDisposable.Dispose called on them.


Note that exit includes normal exit as the code drops through `:EndDisposable`, or if an error occurs and is trapped, or if branch (`→`) is used to exit the block, or anything else.


See also:  .Disposing of .NET Objects.

## Example (Normal Exit)
```apl
:Disposable f←⎕NEW Font
.
.
:EndDisposable
```


In the above example, when the `:EndDisposable` statement is reached, the system disposes of the Font object `f` (and all the resources associated with it) by calling `(IDisposable)f.Dispose()`. A subsequent reference to `f` would generate `VALUE ERROR`.

## Example (Normal Exit)
```apl
:Disposable fonts←⎕NEW ¨Font Font
.
.
:EndDisposable
```


In the above example, Dispose() is called on **each** of the Font objects in `fonts` during the processing of `:EndDisposable`.

## Example (Branch Exit)
```apl
:Disposable fonts←⎕NEW ¨Font Font
.
→0
.
:EndDisposable
```


In this example, Dispose() is called on  the Font objects in `fonts` during the processing of the branch statement `→0`.

## Example (TrapExit)
```apl
:trap 0

   :Disposable fonts←⎕NEW ¨Font Font
   .
   ÷0
   .
   :EndDisposable

:else

   ⎕←'failed'

:endif

```


Here, the objects are disposed of when the `DOMAIN ERROR` generated by the expression `÷0` causes the stack to be cut back to the `:Else` clause. At this point (just before the execution of the `:Else` clause) the name class of `fonts` becomes 0.


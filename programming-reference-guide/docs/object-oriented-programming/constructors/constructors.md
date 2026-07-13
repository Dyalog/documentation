# Constructors

A Constructor is a special function defined in the Class script that is to be run when an Instance of the Class is created by `⎕NEW`. Typically, the job of a Constructor is to initialise the new Instance in some way.

A Constructor is identified by a `:Implements Constructor` statement. This statement may appear anywhere in the body of the function after the function header. The significance of this is discussed below.

Note that it is also *essential* to define the Constructor to be *Public*, with a `:Access Public` statement, because like all Class members, Constructors default to being *Private*. Private Constructors currently have no use or purpose, but it is intended that they will be supported in a future release of Dyalog APL.

A Constructor function may be niladic or monadic and must not return a result.

A Class may specify any number of different Constructors of which one (and only one) may be niladic. This is also referred to as the *default* Constructor.

There may be any number of monadic Constructors, but each must have a differently defined argument list which specifies the number of items expected in the Constructor argument. See ["Constructor Overloading"](constructor-overloading.md) for details.

The only way a Constructor function should be invoked is by `⎕NEW`. See ["Base Constructors"](./base-constructors.md) for further details. If you attempt to call a Constructor function  from outside its Class, it will cause a `SYNTAX ERROR`. A Constructor function should not call another Constructor function within the same Class, although it will not generate an error. This would cause the Base Constructor to be called twice, with unpredictable consequences.

When `⎕NEW` is executed *with a 2-item argument,* the appropriate monadic Constructor is called with the second item of the `⎕NEW` argument.

The niladic (default) Constructor is called when `⎕NEW` is executed with a 1-item argument, a Class reference alone, or whenever APL needs to create a [fill item](../../introduction/arrays/prototypes-and-fill-items.md) for the Class.

Note that `⎕NEW` first creates a new instance of the specified Class, and then executes the Constructor inside the instance.

<h2 class="example">Example</h2>

The `DomesticParrot` Class defines a Constructor function `egg` that initialises the Instance by storing its name (supplied as the 2<sup>nd</sup> item of the argument to `⎕NEW`) in a Public Field called `Name`.
```apl
:Class DomesticParrot: Parrot
    :Field Public Name
    
    ∇ egg name
      :Implements Constructor
      :Access Public
      Name←name
    ∇
    ...
:EndClass ⍝ DomesticParrot

```
```apl
      pol←⎕NEW DomesticParrot 'Polly'
      pol.Name
Polly
```

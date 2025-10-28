<h1 class="heading"><span class="name">Exporting Methods</span></h1>

Your Web Service will be of no use unless it exports at least one method. To export a function as a method, you must include declaration statements. Such declarations may be supplied anywhere within the function body, but it is recommended that they appear together as the first block of statements in your code. All declaration statements begin with the colon (:) character and the following declaration statements are supported:
```apl
:Access WebMethod
```

This statement causes the function to be exported as a method and **must** be present.
```apl
:Signature type ← fnname type name1, type name2, ...
```

This statement declares the data type of the result and the arguments of the method where `type` may specify any valid .NET type that is supported by Web Services. Note that the assignment arrow (`←`) is necessary if the function returns a result.

The declaration of each parameter of the method is separated from the next by a comma. Each `name` may be any ASCII character string. Note that names are optional.

## Add1
```apl
∇ R←Add1 args
 :Access WebMethod
 :Signature Int32←Add Int32 arg1,Int32 arg2
  R←+/args
∇
```

The `Add1` function defined above is exported as a method named `Add`, that takes exactly (and only) two parameters of type `Int32` and returns a result of type `Int32`. Armed with this definition, which is recorded in the metadata associated with the class, the .NET Framework guarantees that the method will only be called in this way.

## Add2
```apl
∇ R←Add2 arg
 :Access WebMethod
 :Signature Double←Add Double[] arg1
  R←+/arg
∇
```

The `Add2` function defined above is exported as a method that takes an array of `Double` and returns a result of type `Double`. Depending on the type of the arguments provided when the method is invoked, .NET and Dyalog will call `Add1` or `Add2` - or generate an exception if the argument does not match any of the signatures.

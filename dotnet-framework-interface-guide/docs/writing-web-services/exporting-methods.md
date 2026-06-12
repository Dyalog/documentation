<h1 class="heading"><span class="name">Exporting Methods</span></h1>

Your web service will not be useful unless it exports at least one method. To export a function as a method, you must include declaration statements. These declarations can be supplied anywhere within the function body, but it is recommended that they appear together as the first block of statements in your code. All declaration statements begin with the colon (`:`) character. The following declaration statements are supported:

- `:Access WebMethod`

    This statement causes the function to be exported as a method and must be present.

- `:Signature type ← fnname type name1, type name2, ...`

    This statement declares the data type of the result and the arguments of the method, where `type` can specify any valid .NET type that is supported by web services. The assignment arrow (`←`) is necessary if the function returns a result.

    The declaration of each parameter of the method is separated from the next by a comma. Each `name` can be any ASCII character string. Names are optional.

## The Add1 Function
```apl
∇ R←Add1 args
 :Access WebMethod
 :Signature Int32←Add Int32 arg1,Int32 arg2
  R←+/args
∇
```

The `Add1` function is exported as a method called `Add` that takes exactly (and only) two parameters of type <code class="language-nonAPL">Int32</code> and returns a result of type <code class="language-nonAPL">Int32</code>. This definition is recorded in the metadata associated with the class, which guarantees that the .NET Framework will only call the method in this way.

## The Add2 Function
```apl
∇ R←Add2 arg
 :Access WebMethod
 :Signature Double←Add Double[] arg1
  R←+/arg
∇
```

The `Add2` function is exported as a method that takes an array of <code class="language-nonAPL">Double</code> and returns a result of type <code class="language-nonAPL">Double</code>. Depending on the type of the arguments provided when the method is invoked, .NET and Dyalog will call `Add1` or `Add2` or generate an exception if the argument does not match either of the signatures.

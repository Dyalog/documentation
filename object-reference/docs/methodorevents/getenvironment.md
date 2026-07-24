# <span>GetEnvironment</span> <span>Method 510</span>

**Description**

This method is used to obtain information about one or more parameters that were specified in the Dyalog command line, your Windows registry, or defined as environment variables. If a value is defined in several places (for example, MAXWS in the command line overriding MAXWS in the registry), GetEnvironment follows exactly the same logic as is used by Dyalog APL itself and so obtains the same value.

The argument to GetEnvironment is a single item as follows:

|-----|-----------------|---------|
|`[1]`|Parameter name(s)|see below|

*Parameter names* is simple character vector or vector of character vectors specifying one or more parameters.

The result is a simple character vector or a vector of character vectors.

<h2 class="example">Examples</h2>
```apl
      GetEnvironment 'MAXWS'
2G

      GetEnvironment ⊂'LOG_SIZE' 'MAXWS'
 16  2G
```

Note that you may use GetEnvironment to obtain the values of your own arbitrary parameters given on the APL command line or specified as environment variables.

GetEnvironment is not supported by DYALOG.DLL because it does not use parameters.

**Application**

Objects: [Root](../objects/root.md)

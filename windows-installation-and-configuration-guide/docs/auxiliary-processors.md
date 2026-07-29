# Auxiliary Processors

## Introduction

Auxiliary Processors (APs) are non-APL programs which provide Dyalog APL users with additional facilities. They run under the control of Dyalog APL.

Typically, APs are used where speed of execution is critical, for utility libraries, or as interfaces to other products. APs may be written in any compiled language, although C is preferred and is directly supported.

Dyalog would recommend that rather than creating APs, customers should now create DLLs (Dynamic Shared Libraries)/shared libraries. If very high performance is required, customers should consider DWA (Direct Workspace Access); contact support@dyalog.com for more information about DWA, including pre-requisite training courses.

## Starting an AP

An Auxiliary Processor is invoked using the dyadic form of `⎕CMD`. The left argument to `⎕CMD` is the name of the program to be executed; the value of the **WSPATH** parameter is used to find the named file. In Dyalog APL/W, the right argument to `⎕CMD` is ignored.
```apl
        'xutils' ⎕CMD ''
```

On locating the specified program, Dyalog APL starts the AP and initialises a memory segment for communication between the workspace and the AP. This communication segment allows data to be passed from the workspace to the other process, and for results to be passed back. The AP then sends APL some information about its external functions (names, code numbers and calling syntax), which APL enters in the symbol table. APL then continues processing while the AP waits for instructions.

## Using the AP

Once established, an AP is used by making a reference to one of its external functions. An external function behaves as if it was a locked defined function, but it is in effect an entry point to the AP. When an external function is referenced, APL transmits a code number to the AP, followed by any arguments. The AP then takes over and performs the desired processing before posting the result back.

## Terminating the AP

An AP is terminated when all the last of its external functions is expunged from the active workspace. This could occur with the use of `)CLEAR`, `)LOAD`, `)ERASE`, `⎕EX`, `)OFF`, `)CONTINUE` or `⎕OFF`.

<h3 class="example">Example</h3>

Start an Auxiliary Processor called `EXAMPLE`. This fixes two external functions called `DATE_TO_IDN` and `IDN_TO_DATE` which deal with the conversion of International Day Numbers to Julian Dates.
```apl
.------------------------.
|      APL PROCESS       |
|------------------------|
|     )CLEAR             |
|clear ws                |
|                        |   start AP  .--------------.
|    'EXAMPLE' ⎕CMD ''   |------------>|  AP EXAMPLE  |
|                        |             |--------------|
|                        | info about  |Send info on  |
|                        |<------------|external fns  |
|                        |  functions  |              |
|    )FNS                |             |  wait ...    |
|DATE_TO_IDN IDN_TO_DATE |             |              |
|                        |function code|              |
|    IDN_TO_DATE 19407   |------------>|call relevant |
|                        |    19407    | subroutine   |
|    wait ...            |             |              |
|                        |<-18 Feb 53--| send result  |
|18 Feb 53               |             |              |
|                        | terminate   |              |
|     )CLEAR             |------------>|     EXIT     |
|clear ws                |  and stop   .--------------.
|                        |
.------------------------.

```

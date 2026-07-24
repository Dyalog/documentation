# `⎕NA` under UNIX

`⎕NA` is fully supported under UNIX; the Conga communications package for example is a shared library on all platforms.

`⎕NA` supports user-written shared libraries and also system-supplied shared libraries. Dyalog APL under UNIX is supplied with a shared library, dyalog32.so or dyalog64.so which contains the same functions as the DLLs which are described in the `⎕NA` documentation in the *Dyalog Language Reference Guide*. Additionally, the function `getlasterror` is included; this returns the error code at the point when the called function failed (which may be different from its value at the point where a previous error occurred).

It is necessary to specify the complete name of the file containing the shared library, no extension is added by Dyalog APL.

When developing code using `⎕NA` it may be useful to set the environment variable ERRORONEXTERNALEXCEPTION= 1. When this is set, Dyalog APL will generate an event 91, `EXTERNAL DLL EXCEPTION` rather than a syserror should a call on a functions defined by `⎕NA` be ill-specified. It should be noted however that the workspace may become corrupt, so it is not recommended to run in production with this variable set.

## System Shared Libraries

On AIX many system library functions appear in libc.a.

When calling system shared libraries under AIX, you must refer to them as:

64-bit: libc.a(shr_64.o)

32-bit: libc.a(shr.o)

It is not always possible to access all library functions - on AIX for example it is not possible to access memcpy() or strncpy(). it is for this reason that dyalog*.so includes MEMCPY and STRNCPY.

On Linux, it is a little more difficult to locate the libc.so file; the function `libc` in the supplied workspace quadna (which contains two namespaces, `Windows` and `NonWindows`) can be used to locate this file.

### Definitions

In the remainder of this section references are made to the APL variables `sharedlib` and `dyalib`; the definitions for both vary between AIX and Linux, and between 32 and 64 bit interpreters.

Under AIX, `sharedlib` is defined as:
```apl
      sharedlib←'libc.a(shr_64.o)' ⍝ 64 bit
      sharedlib←'libc.a(shr.o)'    ⍝ 32 bit  
```

Under Linux, it is necessary to identify the shared library:
```apl
      )COPY quadna NonWindows.libc
      sharedlib←libc ⍬
```

For all UNIX platforms, the dyalog shared library is identified as
```apl
      dyalib←'dyalog64.so'         ⍝ 64 bit
      dyalib←'dyalog32.so'         ⍝ 32 bit
	
```

## Example 1

getpid() is common to all UNIX platforms; it returns an int which is the process ID of the current process. It is defined to be

pid_t getpid(void)

where pid_t is a 4-byte integer.

The APL code to instantiate this function is
```apl

      ⎕NA 'I4 ',sharedlib,'|getpid'
		
```

## Example 2

This is a slightly more complex example, which uses the STRNCPY function in the Dyalog-supplied shared library to retrieve the value of a variable which is referenced by a pointer, returned from the system library function:

getenv()returns a pointer to the value of the environment variable which is the argument of the function. It is defined to be

char *getenv(const char *name)
```apl

      ∇r←GetEnv envvar;getenv;P;get
       r←''
       ⎕NA'P ',sharedlib,'|getenv <0T1[]'
       'get'⎕NA dyalib,'|STRNCPY >0U1[] P U4'
       P←getenv⊂'UTF-8'⎕UCS ⎕UCS envvar
       →0⍴⍨P=0
       r←'UTF-8'⎕UCS get 4096 P 4096
      ∇

      GetEnv'MAXWS'
4G	
```

!!! note
    The call to STRNCPY has been defined to return a vector of integers so that the result can be passed directly to `⎕UCS`.

## geterrno

The dyalog shared libary under UNIX includes the function `geterrno`. This returns the current value of errno; be aware that it may not have the same value as at the point when the error was raised. To use this function:
```apl

      ⎕NA 'I ',dyalib,'|geterrno'
      geterrno
5
      		
```

## Shared libraries and APL threads

Any shared library function must mask out all signals for  new threads which it creates. Failure to do so will result in a catastrophic failure of APL's signal handling.

<h1 class="heading"><span class="name">Core and aplcore files</span></h1>

When Dyalog APL encounters an unexpected problem it is likely that the interpreter will terminate and generate either a core file or an aplcore file. Under Linux core files are not created by default; it is necessary to enable their creation.

An aplcore file contains the workspace at the point where the interpreter terminated, along with debug information that may enable Dyalog to identify and rectify the problem.

The Dyalog support department (support@dyalog.com, other means of contact on the Dyalog website) should be contacted if an aplcore file is generated. More immediately it may be possible to copy the contents of the aplcore into a new Dyalog process by running
```apl
      )COPY aplcore
```

Note however that it is possible that the `)COPY` itself will cause another aplcore; it is best to rename the original aplcore before attempting this course of action.

From Version 13.2 onwards in situations where a core file is generated, an aplcore file will be generated too; this is done by forking the failing APL process, so an additional APL process will appear in any process listing while the aplcore is being created. If the environment variable *APL_TEXTINAPLCORE* is set and has the value 1 then an "Interesting Information" section is appended to the aplcore which contains information such as the APL stack, the WSID of the originating workspace etc. This section can be extracted from an aplcore using
```apl
sed -n '/======== Interesting Information/,$p' aplcore
```

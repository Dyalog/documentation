# The web.config File

ASP.NET configuration parameters are defined in a file called **web.config** located in or above the root directory of an ASP.NET application. Parameters defined in these files supplement or override ASP.NET parameters that are defined system-wide.

The **web.config** file provided with Dyalog is located in **[DYALOG]\Samples\asp.net** and applies to all the examples residing in child directories of this directory. If you create a Dyalog ASP.NET application elsewhere on your system, you will need to copy  **web.config** into the application root directory. The parameters defined in the **web.config** file are (further details are provided in comments in the file):

- <code class="language-nonAPL">DyalogBinDirectory</code><br />This specifies the full path to the Dyalog binaries (DLLs and script compiler).

- <code class="language-nonAPL">dyalog (compiler)</code><br />This section defines an ASP.NET language named <code class="language-nonAPL">dyalog</code>; the expression  <code class="language-nonAPL">Language = "dyalog"</code> in a script file associates that script with the Dyalog .NET Compiler **dyalogc.exe**. Subsidiary parameters and keys for the <code class="language-nonAPL">dyalog</code> compiler are:

- <code class="language-nonAPL">debug</code> – "true" (default)  to bind the script to the Development DLL, or "false" to bind the script to the run-time DLL

<code class="language-nonAPL">DyalogCompilerEncoding</code> – "classic" or "unicode"

<code class="language-nonAPL">DyalogCompilerOptions</code> – defines options for the script compiler, for example, to set `⎕WX`to 1, use "`/wx:1`"

<code class="language-nonAPL">DyalogCompilerEmitPragmas</code> – set to "true" if you are using workspace behind (for more information on workspace behind, see [xxx](workspace-behind.md))

- <code class="language-nonAPL">debug</code> – "true" (default)  to bind the script to the Development DLL, or "false" to bind the script to the run-time DLL
- <code class="language-nonAPL">DyalogCompilerEncoding</code> – "classic" or "unicode"
- <code class="language-nonAPL">DyalogCompilerOptions</code> – defines options for the script compiler, for example, to set `⎕WX`to `1`, use "`/wx:1`"
- <code class="language-nonAPL">DyalogCompilerEmitPragmas</code> – set to "true" if you are using workspace behind (for more information on workspace behind, see [xxx](workspace-behind.md))

- <code class="language-nonAPL">DyalogIsolationMode</code><br />This parameter specifies the isolation method. For more information on isolation modes, see [Isolation Mode](isolation-mode.md)

- <code class="language-nonAPL">DyalogCacheDirectory</code><br />This parameter defines the directory in which to save cached files.

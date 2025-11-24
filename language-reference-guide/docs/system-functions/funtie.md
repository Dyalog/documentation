---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FUNTIE FUNTIE
</div>






<h1 class="heading"><span class="name">File Untie</span> <span class="command">{R}←⎕FUNTIE Y</span></h1>



`Y` must be a simple integer scalar or vector (including Zilde).  Files whose tie numbers occur in `Y` are untied.  Other elements of `Y` have no effect.


If `Y` is empty, no files are untied, but all the interpreter's internal file buffers are flushed and the operating system is asked to flush all file updates  to disk.  This special facility allows the programmer to add extra security (at the expense of performance) for application data files.


The shy result of `⎕FUNTIE` is a vector of tie numbers of the files **actually untied**.

<h2 class="example">Example</h2>
```apl
      ⎕FUNTIE ⎕FNUMS ⍝ Unties all tied files
 
      ⎕FUNTIE ⍬      ⍝ Flushes all buffers to disk
```




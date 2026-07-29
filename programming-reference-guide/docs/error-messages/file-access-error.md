

# <span>FILE ACCESS ERROR</span> `19`

This report is given when the user attempts to execute a file system function for which the user is not authorised, or has supplied the wrong passnumber.  It also occurs if the file specified as the argument to `⎕FERASE` or `⎕FRENAME` is not exclusively tied.

<h2 class="example">Examples</h2>
```apl
      'SALES' ⎕FSTIE 1
 
      ⎕FRDAC 1
0 4121 0
0 4137 99
 
      X ⎕FREPLACE 1
FILE ACCESS ERROR
      X ⎕FREPLACE 1
      ^
 
      'SALES' ⎕FERASE 1
FILE ACCESS ERROR
      'SALES' ⎕FERASE 1
      ^
```

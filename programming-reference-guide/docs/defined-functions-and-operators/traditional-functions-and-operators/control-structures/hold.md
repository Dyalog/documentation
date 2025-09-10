




<h1 class="heading"><span class="name">Hold Statement</span> <span class="command">:Hold tkns</span></h1>



[Formal Definition](hold-statement-definition.md){: .noprint }


Whenever more than one thread tries to access the same piece of data or shared resource at the same time, you need some type of synchronisation to control access to that data. This is provided by `:Hold`.



`:Hold` provides a mechanism to control thread entry into a critical section of code. `tkns` must be a simple character vector or scalar, or a vector of character vectors. `tkns` represents a set of "tokens", all of which must be acquired before the thread can continue into the control structure. `:Hold` is analogous to the component file system `⎕FHOLD` which is used to synchronise access between **processes**. See also [File Hold](../../../../../earlier-release-notes/release-notes-v19-0/language-reference-changes/fhold).


Within the whole active workspace, a token with a particular value may be held only once. If the hold succeeds, the current thread *acquires* the tokens and execution continues with the first phrase in the control structure. On exit from the structure, the tokens are released for use by other threads. If the hold fails, because one or more of the tokens is already in use:

1. If there is no `:Else` clause in the control structure, execution of the thread is blocked until the requested tokens become available.
2. Otherwise, acquisition of the tokens is abandoned and execution resumed immediately at the first phrase in the `:Else` clause.


`tkns` can be either a single token:
```apl
    'a'
    'Red'
    '#.Util'
    ''
    'Program Files'
```


… or a number of tokens:
```apl
    'red' 'green' 'blue'
    'doe' 'a' 'deer'
    ,¨'abc'
    ↓⎕NL 9
```


Pre-processing removes trailing blanks from each token before comparison, so that, for example, the following two statements are equivalent:
```apl
    :Hold 'Red' 'Green' 
    :Hold ↓2 5⍴'Red  Green'
```


Unlike `⎕FHOLD`, a thread does not release all existing tokens before attempting to acquire new ones. This enables the nesting of holds, which can be useful when multiple threads are concurrently updating parts of a complex data structure.


In the following example, a thread updates a critical structure in a child namespace, and then updates a structure in its parent space. The holds will allow all "sibling" namespaces to update concurrently, but will constrain updates to the parent structure to be executed one at a time.
```apl
    :Hold ⎕CS''          ⍝ Hold child space     
        ...              ⍝ Update child space
        :Hold ##.⎕CS''   ⍝ Hold parent space 
            ...          ⍝ Update Parent space
        :EndHold
        ...
    :EndHold
```


However, with the nesting of holds comes the possibility of a "deadlock". For example, consider the two threads:


|Thread 1                                                                           |Thread 2                                                                           |
|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
|<pre><code>:Hold 'red'<br/>     ...<br/>     :Hold 'green'<br/>         ...<br/>     :EndHold<br/> :EndHold</code></pre>|<pre><code>:Hold 'green'<br/>     ...<br/>     :Hold 'red'<br/>         ...<br/>     :EndHold<br/> :EndHold</code></pre>|


In this case if both threads succeed in acquiring their first hold, they will both block waiting for the other to release its token.


If this deadlock situation is detected acquisition of the tokens is abandoned. Then:

1. If there is an `:Else` clause in the control structure,  execution jumps to the `:Else` clause.
2. Otherwise, APL issues an error `(1008) DEADLOCK`.


You can avoid deadlock by ensuring that threads always attempt to acquire tokens in the same chronological order, and that threads never attempt to acquire tokens that they already own.


Note that token acquisition for any particular `:Hold` is atomic, that is, either *all* of the tokens or *none* of them are acquired. The following example *cannot* deadlock:


|Thread 1                                                                           |Thread 2                                              |
|-----------------------------------------------------------------------------------|------------------------------------------------------|
|<pre><code>:Hold 'red'<br/>     ...<br/>     :Hold 'green'<br/>         ...<br/>     :EndHold<br/> :EndHold</code></pre>|<pre><code>:Hold 'green' 'red'<br/>     ...<br/>     :EndHold</code></pre>|

<h2 class="example">Examples</h2>


`:Hold` could be used for example, during the update of a complex data structure that might take several lines of code. In this case, an appropriate value for the token would be the name of the data structure variable itself, although this is just a programming convention: the interpreter does not associate the token value with the data variable.
```apl
    :Hold'Struct'
        ...              ⍝ Update Struct
        Struct ← ...
    :EndHold
```


The next example guarantees exclusive use of the current namespace:
```apl
    :Hold ⎕CS''          ⍝ Hold current space
        ...
    :EndHold
```


The following example shows code that holds two positions in a vector while the contents are exchanged.
```apl
    :Hold ⍕¨to fm
        :If >/vec[fm to]
            vec[fm to]←vec[to fm]
        :End
    :End
```


Between obtaining the next available file tie number and using it:
```apl
    :Hold '⎕FNUMS'
        tie←1+⌈/0,⎕FNUMS
        fname ⎕FSTIE tie
    :End
```


The above hold is not necessary if the code is combined into a single line:
```apl
    fname ⎕FSTIE tie←1+⌈/0,⎕FNUMS
```


or,
```apl
    tie←fname ⎕FSTIE 0
```


Note that `:Hold`, like its component file system counterpart `⎕FHOLD`, is a device to enable *co-operating* threads to synchronise their operation.


`:Hold` does not *prevent* threads from updating the same data structures concurrently, it prevents threads only from `:Hold`ing the same tokens.

## High-Priority Callbacks


`:Hold`
 with a non-zero number of tokens is not permitted in a high-priority callback and an attempt to use it  will cause the error:
```apl
 DOMAIN ERROR: Cannot :Hold within high priority callback
```



See [High-Priority Callback Functions](../../../../../interface-guide/introduction/high-priority-callbacks).




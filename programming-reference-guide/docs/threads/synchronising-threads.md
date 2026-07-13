# Synchronising Threads

Threads may be synchronised using *tokens* and a *token pool*.

An application can synchronise its threads by having one thread add tokens into the pool whilst other threads wait for tokens to become available and retrieve them from the pool.

Tokens possess two separate attributes, a *type* and a *value*.

The *type* of a token is a positive or negative numeric scalar. The *value* of a token is any arbitrary array that you might wish to associate with it.

The token pool may contain up to 2*31 tokens; they do not have to be unique neither in terms of their types nor of their values.

The following system functions are used to manage the token pool:

|---------|---------------------------------------------------------------------|
|`⎕TALLOC`|Allocates ranges of tokens.                                          |
|`⎕TPUT`  |Puts tokens into the pool.                                           |
|`⎕TGET`  |If necessary waits for, and then retrieves some tokens from the pool.|
|`⎕TPOOL` |Reports the types of tokens in the pool                              |
|`⎕TREQ`  |Reports the token requests from specific threads                     |

A simple example of a thread synchronisation requirement occurs when you want one thread to reach a certain point in processing before a second thread can continue. Perhaps the first thread performs a calculation, and the second thread must wait until the result is available before it can be used.

This can be achieved by having the first thread put a specific type of token into the pool using `⎕TPUT`. The second thread waits (if necessary) for the new value to be available by calling `⎕TGET` with the same token type.

Notice that when `⎕TGET` returns, the specified tokens are *removed* from the pool. However, *negative* token types will satisfy an infinite number of requests for their positive equivalents.

The system is designed to cater for more complex forms of synchronisation. For example, a *semaphore* to control a number of resources can be implemented by keeping that number of tokens in the pool. Each thread will take a token while processing, and return it to the pool when it has finished.

A second complex example is that of a *latch* which holds back a number of threads until the coast is clear. At a signal from another thread, the latch is opened so that all of the threads are released. The latch may (or may not) then be closed again to hold up subsequently arriving threads. A practical example of a latch is a ferry terminal.

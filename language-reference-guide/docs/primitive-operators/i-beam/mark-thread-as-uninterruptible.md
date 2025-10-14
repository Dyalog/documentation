
<!-- Hidden search keywords -->
<div style="display: none;">
  2503⌶
</div>






<h1 class="heading"><span class="name">Mark Thread as Uninterruptible</span> <span class="command">R←2503⌶Y</span></h1>



This function marks the current thread (the thread in which it is called) as uninterruptible, and/or determines whether or not any child threads, subsequently created by the current thread, will be uninterruptible.


The right argument `Y` is an integer whose value is the sum of the following (bit-wise) values:

- 1 : mark thread as uninterruptible
- 2 : mark its children as uninterruptible


The result `R` is an integer value that indicates the previous state of the thread.


In many multi-threaded applications a large proportion of the threads are used for communication mechanisms (`⎕DQ` on TCPSockets, Conga, isolates); but most of the "real work" is done in thread zero.


It is undesirable that a weak interrupt interrupts a seemingly random thread. The mechanism to prevent a thread from being (weak) interrupted allows an application to be configured so that only specific threads would respond to a weak interrupt.




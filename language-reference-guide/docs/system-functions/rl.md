---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕RL RL
</div>






# <span>Random Link</span> `⎕RL`



`⎕RL` is a 2-element vector. Its first element contains the  base or *random number seed* and its second element is an integer that identifies the random number generator that is currently  in use. Together these items define how the system generates random numbers using [Roll](../primitive-functions/roll.md) and [Deal](../primitive-functions/deal.md).


In a `clear ws` `⎕RL` is `(⍬ 1)`. `⎕RL` has Namespace scope.


## Random Number Seed


The facility to set the seed to a specific value provides the means to generate a repeatable sequence of random numbers, such as might be required by certain types of simulation modelling. This capability is not provided by RNG2.


If the seed is set to 0, the seed is set randomly but may be retrieved and subsequently re-assigned to create a repeatable sequence.


If the seed is set to `⍬`, Dyalog is able to take advantage of certain optimisations which deliver maximum performance. In this case, the actual seed in use is intentionally hidden and `⎕RL[1]` always reports `⍬`, regardless of the Random Number Generator in use.

## Random Number Generators


The 3 random number generators are listed in the table below. The 4th column of the table contains the values of seeds that may be assigned to them.


|Id |Name|Algorithm                                |Valid Seed Values                                                                 |
|---|----|-----------------------------------------|----------------------------------------------------------------------------------|
|0  |RNG0|Lehmer linear congruential generator.    |`0` , `⍬` , or an integer in the range 1 to `¯2+2*31`                             |
|1  |RNG1|Mersenne Twister.                        |`0` , `⍬` , an integer in the range 1 to `¯1+2*63` or a 625-element integer vector|
|2  |RNG2|Operating System random number generator.|`⍬`                                                                               |


Note that assigning an invalid value to the seed will cause `DOMAIN ERROR`.


The default random number generator in a `CLEAR WS` is 1 (Mersenne Twister). This algorithm *RNG1* produces 64-bit values with good distribution.


The Lehmer linear congruential generator *RNG0* was the only random number generator provided in versions of Dyalog APL prior to Version 13.1. The implementation of this algorithm has several limitations including limited value range `(2*31)`, short period and non-uniform distribution (some values may appear more frequently than others). It is retained for backwards compatibility.


Under Windows, the Operating System random number generator algorithm *RNG2* uses the `rand_s()` function. Under UNIX/Linux it uses `/dev/urandom`.

## Random Number Sequences


Random number sequences may be predictable or not and  repeatable or not. A predictable and repeatable sequence is obtained by starting with the same specific value for the seed. A non-predictable sequence is obtained by starting with a seed which is itself chosen at random, but such a sequence is repeatable if the value of the seed (chosen at random) is visible. A non-predictable and non-repeatable sequence of random numbers is obtained where the initial seed is chosen completely at random and is unknown.


Using  *RNG0* or *RNG1*:

- To obtain  an entirely predictable random sequence, set the seed to a non-zero value
- To obtain a non-predictable, but repeatable sequence, set the seed to `0`
- To obtain a non-predictable, non-repeatable series of random numbers, set the seed to `⍬`


*RNG2* does not support a user modifiable random number seed, so when using this scheme, it is not possible to obtain a repeatable random number series and the seed must always be `⍬`.

## Implementation Note


`⎕RL` does not behave quite like a regular 2-element variable; it has its own rules relating to assignment and reference.

### Reference


`⎕RL` *returns* a 2-element vector whose second element identifies the scheme in use (0, 1 or 2).


If  `⎕RL[1]` is set to `⍬`,  `⎕RL[1]`always reports `⍬`.



Otherwise if the seed `⎕RL[1]` is set to a value other than `⍬`:

- using *RNG0*, `⎕RL[1]` is an integer which  represents the *seed* for the next random number in the sequence.
- using *RNG1*, the system internally retains a block of 312 64-bit numbers which are used one by one to generate the results of roll and deal. When the first block of 312 have been used up, the system generates a second block. In this case, `⎕RL[1]` is an integer vector of 32-bit numbers of length 625 (the first is an index into the block of 312) which represents the internal state of the random number generator. This means that, as with *RNG0*, you may save the value of  `⎕RL` in a variable and reassign it later.
- Using *RNG2*, the seed is purely internal and `⎕RL[1]` is always zilde.


### Assignment


`⎕RL` may only be assigned in its entirety. Indexed and selective assignment may not be used to assign values to individual elements.


To preserve compatibility with Versions of Dyalog prior to Version 15.0 (in which `⎕RL` specifies just the seed) if the value assigned to `⎕RL` represents a valid seed for the random number generator in use, it is taken to be the new seed. Otherwise, the value assigned to `⎕RL` must be a 2-element vector, whose first item is the seed and whose second item is 0, 1 or 2 and specifies the random number generator to be used subsequently.

## Examples (specific seeds for repeatable sequences)
```apl

      )CLEAR
clear ws
      ⎕RL←16807 
      10?10      
4 1 6 5 2 9 7 10 3 8
      5↑⊃⎕RL       
10 0 16807 1819658750 ¯355441828
      X←?1000⍴1000 
      5↑⊃⎕RL       
100 ¯465541037 ¯1790786136 ¯205462449 996695303
```
```apl

      ⎕RL←16807
      10?10      
4 1 6 5 2 9 7 10 3 8
      Y←?1000⍴1000 
      X≡Y
1
      5↑⊃⎕RL       
100 ¯465541037 ¯1790786136 ¯205462449 996695303  
```
```apl

      ⎕RL←16807 0 ⍝ Select RNG0
      ⎕RL
16807 0
      ?9 9 9
2 7 5
      ?9
7
      ⎕RL
984943658 0

      ⎕RL←16807
      ?9 9 9
2 7 5
      ?9
7
      ⎕RL
984943658 0
```
```apl

      ⎕RL←16807 1 ⍝ Select RNG1
      5↑⊃⎕RL
100 ¯465541037 ¯1790786136 ¯205462449 996695303

```

### Examples (0 seed)


When you set the seed to 0, a random seed is created for you:
```apl
      ⎕RL←0 0
      ⎕RL
865618822 0
      ⎕RL←0
      ⎕RL
1100783275 0
```


Setting the seed to 0 gives you a new, unpredictable random sequence yet it is repeatable because you can retrieve (and subsequently re-use) the actual seed after you set it:
```apl
      ?10⍴100
14 22 18 30 42 22 71 32 32 12
      ⎕RL←1100783275
      ?10⍴100
14 22 18 30 42 22 71 32 32 12
```

### Example (zilde)


When you set the seed to zilde, you get the same random initialisation as setting it to 0 but you can't retrieve the actual value of the seed. When it is  set to `⍬` it is subsequently reported as `⍬` and the internal value of the seed is hidden.
```apl
      ⎕RL←⍬
      ⎕RL
┌┬─┐
││0│
└┴─┘
```



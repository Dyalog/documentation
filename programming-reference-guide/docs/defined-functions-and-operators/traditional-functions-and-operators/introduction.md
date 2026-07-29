# Traditional Functions and Operators

*Traditional* Functions and Operators are the original user-defined functions and operators that are part of the APL standard. They are referred to herein as *Traditional* or *TradFns* to distinguish them from Dfns and Dops which are unique to Dyalog.

*TradFns* may be defined and edited using the Dyalog Editor or may be instantiated from an array containing source code using the system function `⎕FX`. The converse system functions `⎕CR`, `⎕VR`, `⎕NR` return the original source code.

A defined function or operators is composed of lines.  The first line (line 0) is called the *header*. Remaining lines are APL statements, called the *body*.

The header consists of the following parts:

1. its model syntactical form,
2. an optional list of local names, each preceded by a semi-colon (`;`) character,
3. an optional comment, preceded by the symbol `⍝`.

Only the model is required. If local names and comments are included, they must appear in the prescribed order.

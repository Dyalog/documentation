




# <span>DEADLOCK</span> `1008`



If two threads succeed in acquiring a hold of two different tokens, and then each asks to hold the other token, they will both stop and wait for the other to release its token. The interpreter detects such cases and issues an error (1008) `DEADLOCK`.




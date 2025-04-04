<h1 class="heading"><span class="name">Stream Sockets</span></h1>



A Stream socket is a connection-based transport that is analogous to a telephone service. A Stream socket handles error correction, guarantees delivery, and preserves data sequence. This means that if you send two messages to a recipient, the messages are sure to arrive and in the sequence that you sent them. However, individual messages may be broken up into several packets (or accumulated into one), and there is no predetermined protocol to identify message boundaries. This means that Stream-based applications must implement some kind of message protocol that both ends of a connection understand and adhere to.



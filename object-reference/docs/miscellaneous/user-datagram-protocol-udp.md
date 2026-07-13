# User Datagram Protocol (UDP)



User Datagram Protocol (UDP) is a connection-less transport mechanism that is somewhat similar to a postal service. It permits a sending application to transmit a message or messages to a recipient. It neither guarantees delivery nor acknowledgment, nor does it preserve the sequence of messages. Messages are also limited to fit into a single packet which is typically no more than 1500 bytes in size. However, a UDP message will be delivered in its entirety.


You may wonder why anybody would use a service that does not guarantee delivery. The answer is that although UDP is technically an unreliable service, it is perfectly possible to implement reliable applications on top of it by building in acknowledgments, time-outs and re-transmissions.



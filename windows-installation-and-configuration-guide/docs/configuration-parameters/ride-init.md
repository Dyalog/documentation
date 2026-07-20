# RIDE_Init

This parameter determines how the interpreter should behave with respect to the Ride protocol. Setting this configuration parameter on the machine that hosts the interpreter enables the interpreter-Ride connection.

RIDE_Init can only be used to specify a limited number of Ride configuration options; the rest must be specified in a Ride ini file. Full details describing how to configure Ride, including using certificates to authenticate connections can be found in the [Ride User Guide](https://dyalog.github.io/ride).

The format of the value is:
```
<setting> : <address> : <port>
```

*setting* is the action the interpreter should take. Valid values, which are case-insensitive, are as follows:

- serve – listen for incoming connections
- http - listen for an incoming request for Zero Footprint Ride
- connect – connect to the specified Ride and end the session if this fails
- poll – try to connect to the specified Ride at regular intervals and reconnect if the connection is lost
- config - specifies the name of the Ride ini file to be used

For serve and http, &lt;address> is a list of IPv4 or IPv6 addresses and/or DNS names of interfaces in the machine where the APL process is running, and specifies the interfaces through which incoming requests to connect are accepted. If &lt;address> is empty, incoming requests are accepted only from the machine itself (the interpreter will listen on the loopback addresses only). If &lt;address> is set to “*” then the interpreter will listen for requests through all the available interfaces in the local machine.

If *setting* is `serve` or `http` then *address*  is a list of IPv4 or IPv6 addresses and/or DNS names of interfaces in the machine where the APL process is running, and specifies the interfaces through which incoming requests to connect are accepted. If *address* is empty, incoming requests are accepted only from the machine itself (the interpreter will listen on the loopback addresses only). If *address* is set to “*” then the interpreter will listen for requests through all the available interfaces in the local machine.

If *setting* is `connect` or `poll` then *address* is an IP address or DNS name of an interface in a remote machine to which the interpreter should attempt to connect. Valid address values are:

- a resolvable name
- an IPv4 or IPv6 address
- empty – the local machine only
- * - (valid only when setting is serve or http) the interpreter listens on all local network interfaces

*port* is the TCP port to listen on

Settings specified by the **RIDE_Init** configuration parameter take precedence over the same setting specified in the Ride ini file. Note that the **RIDE_Init** configuration parameter can specify both *config* and one of *serve*, *http*, *connect* or *poll*. For example,
```
RIDE_INIT=serve:*:4502,config=/home/andys/.dyalog/secureride.ini
```

This is most useful when multiple interpreters need to be run, each with its own Ride connection as each must have a separate port number.

Note that the **RIDE_Init** configuration parameter is set automatically when launching a new Dyalog Session from Ride.

<h2 class="example">Examples</h2>

To allow an incoming connection through any interface in the machine running the interpreter:
```
RIDE_INIT=serve:*:4052
```

To allow incoming Zero Footprint Ride connection through just one interface of the machine running the interpreter:
```
RIDE_INIT=http:192.168.0.10:8080
```

To attempt to connect to Ride running on my colleague's machine:
```
RIDE_INIT=connect:pete.dyalog.com:4052
```

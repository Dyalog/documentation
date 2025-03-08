<h1 class="heading"><span class="name">UUID Generator</span> <span class="command">R←120⌶Y</span></h1>

This function generates a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) (Universally Unique IDentifier) according to the [RFC 9562](https://datatracker.ietf.org/doc/html/rfc9562) specification.

A UUID is a label used to uniquely identify objects in computer systems and does not depend on a central registration authority or coordination between the parties generating them. UUIDs are also known as GUIDs (Globally Unique IDentifiers).

`Y` specifies the UUID Version required.

|`Y`| Version                                                       |
|---|---------------------------------------------------------------|
| 4 | UUIDv4: random values                                         |
| 7 | UUIDv7: time-ordered (based on Unix Epoch) plus random values |

Other values are either unsupported, undefined or reserved.

The result `R` is a vector containing the generated 36-character UUID.

<h2 class="example">Example</h2>
```apl
      120⌶4
32cd549f-eb33-4457-bf45-babf26dc2b53
```

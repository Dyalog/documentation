<h1 class="heading"><span class="name">Language Changes</span></h1>

The following table summarises the main changes to language features in Version 19.0.

|Function/Operator|Description                                                                                           |Change                                                               |
|-----------------|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
|`⎕TALLOC`        |[Allocate Token Range](./talloc.md)                                                                   |New system function                                                  |
|`2000⌶`          |[Memory Management Statistics](./memory-manager-statistics.md)                                        |Extended I-beam function                                             |
|`219⌶`           |Compress Vector of Short Integers                                                                     |Extended I-beam function                                             |
|`1302⌶`          |[Set aplcore Parameters](https://help.dyalog.com/19.0/index.htm#Language/I%20Beam%20Functions/Set%20aplcore%20Parameters.htm)|New I-beam function                                                  |
|`3012⌶`          |[Enable Compression of Large Components](./enable-compression-of-large-components.md)                 |New I-beam function                                                  |
|`5171⌶`          |[Discard Source Information](./discard-source-information.md)                                         |New I-beam function                                                  |
|`5172⌶`          |[Discard Source Code](./discard-source-code.md)                                                       |New I-beam function                                                  |
|`8468⌶`          |[Hash Table Size](./hash-table-size.md)                                                               |New I-beam function                                                  |
|`8469⌶`          |[Lookup Table Size](./lookup-table-size.md)                                                           |New I-beam function                                                  |
|`⎕NCOPY`         |Native File Copy                                                                                      |New [ProgressCallback](../introduction/extension-to-native-file-functions.md) variant|
|`⎕NMOVE`         |Native File Move                                                                                      |New [ProgressCallback](../introduction/extension-to-native-file-functions.md) variant|
|`⎕FHOLD`         |File Hold                                                                                             |New left argument to specify a time-out                              |
|`⎕SIGNAL`        |Signal event                                                                                          |Now accepts 1006 ( `TIMEOUT` error)                                  |

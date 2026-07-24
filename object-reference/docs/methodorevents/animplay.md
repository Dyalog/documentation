# <span>AnimPlay</span> <span>Method 292</span>

**Description**

The AnimPlay method plays an AVI clip in an Animation object.

The argument to AnimPlay is a 3-element array as follows:

|-----|------|-------|
|`[1]`|Repeat|integer|
|`[2]`|From  |integer|
|`[3]`|To    |integer|

*Repeat* specifies the number of times the clip is repeated. A value of -1 causes the clip to be repeated indefinitely.

*From* is a 0-based index of the frame where playing begins and must be less than 65536. A value of zero means begin with the first frame in the AVI clip

*To* is a 0-based index of the frame where playing ends and must be less than 65536. A value of -1 means end with the last frame in the AVI clip

The last frame remains displayed until the clip is unloaded using [AnimClose](./animclose.md) or until another clip is loaded.

**Application**

Objects: [Animation](../objects/animation.md)

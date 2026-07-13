# File Associations

During installation, `setup.exe` associates a number of file extensions with Dyalog applications.

Workspace files with extension `.dws` and files with extension `.dyapp`, which are used to bootstrap [SALT-based applications](https://docs.dyalog.com/latest/SALT%20User%20Guide.pdf#page=12), are associated with `dyalog.exe`.

The following file types are associated with the Dyalog APL Editor `dyaedit.exe`. They are used by various source code management tools, including [Link](https://dyalog.github.io/link/3.0/) and [SALT](https://docs.dyalog.com/latest/SALT%20User%20Guide.pdf) and 3rd party tools like [Acre Desktop](https://github.com/the-carlisle-group/Acre-Desktop/wiki).

|---------|------------|
|`.aplf`  |`Functions` |
|`.aplo`  |`Operators` |
|`.apln`  |`Namespaces`|
|`.aplc`  |`Classes`   |
|`.apli`  |`Interfaces`|
|`.dyalog`|`Generic`   |

Additionally, Link uses `.apla` files to store serialised arrays. These are likely to become associated with `dyaedit.exe` in a future release.

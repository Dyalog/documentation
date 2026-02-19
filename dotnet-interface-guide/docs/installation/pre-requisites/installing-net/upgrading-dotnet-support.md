# Upgrading .NET Support

Dyalog v20.0 supports .NET v8.0 and later, but is configured to support .NET v8.0 by default. To support a later version of .NET, the following files need to be amended (this requires administrator rights) – in each case, the reference to "8.0" or "8.0.0" should be updated to the correct major version number:

- **[DYALOG]/Dyalog.Net.Bridge.deps.json**

`"runtimeTarget": { "name": ".NETCoreApp,Version=v8.0",`

`"targets": { ".NETCoreApp,Version=v8.0": {`

- `"runtimeTarget": { "name": ".NETCoreApp,Version=v8.0",`

- `"targets": { ".NETCoreApp,Version=v8.0": {`

- **[DYALOG]/Dyalog.Net.Bridge.runtimeconfig.json**

`"runtimeOptions": { "tfm": "net8.0", "framework": { "name": "Microsoft.NETCore.App", "version": "8.0.0"`

- `"runtimeOptions": { "tfm": "net8.0", "framework": { "name": "Microsoft.NETCore.App", "version": "8.0.0"`

The replacement version number can also be that of a .NET Release Candidate. For example, if you have downloaded .NET 10.0.0-rc.2, the version number in the aforementioned locations should be set to:

- 10.0 instead of 8.0 (three occurrences)

- 10.0.0-rc.2.25502.107 instead of 8.0.0 (one occurrence).

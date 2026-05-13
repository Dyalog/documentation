<h1 class="heading"><span class="name">Limitations</span></h1>

## Fundamental Limitations

Despite the benefits offered by shared code files, they will not replace the standard Dyalog workspace due to some fundamental limitations.

### Restriction 1

__Shared code files are read only__

Multiple processes can memory-map shared code files simultaneously; each process that uses a shared code file is using the contents of that shared code file directly as memory. This means that a shared code file cannot be updated while it is in use. Instead, when an application modifies an object that resides in a shared code file, a copy of the relevant part of the shared code file is made in workspace memory and the original file is not modified.

### Restriction 2

__Shared code files each have a fixed virtual memory address__

A shared code file contains pointers to absolute memory locations contained within it. This means that the virtual memory address to which it is memory mapped must be fixed when the memory-mapping occurs. When a shared code file is created, a parameter specifies the virtual memory address at which it will be loaded and all pointers contained within it are adjusted to fit this address. If an application uses more than one shared code file, each shared code file must have a different address.

### Restriction 3

__Shared code files cannot be shared across architectures__

A shared code files cannot be converted in any way when it is used. This means that, unlike workspaces, component files, and arrays transmitted using TCP objects or Conga, shared code files cannot be shared between different platforms or versions of Dyalog.

### Restriction 4

__Shared code files are not workspaces__

A shared code file is not a workspace; it is not possible to [`⎕CY`](../../language-reference-guide/system-functions/cy.md) or [`)COPY`](../../language-reference-guide/system-commands/copy.md) from them.

### Restriction 5

__64-bit Unicode only__

The benefits of memory mapping are only realisable in 64-bit address spaces. This, combined with the other fundamental limitations, means that shared code files are only supported for 64-bit Unicode systems; there are no current plans to extend this support.

## Temporary Limitations

There are several restrictions when using shared code files that could be removed in future Dyalog versions.

### Restriction 1

__All objects saved must be visible from the root of the current workspace__

The following cannot be saved in a shared code file:

- GUI namespaces and their derivatives
- Functions created by starting an auxiliary processor
- External functions created using name association ([`⎕NA`](../../language-reference-guide/system-functions/na.md))
- [`⎕SM`](../../language-reference-guide/system-functions/sm.md)

### Restriction 2

__It is not possible to have more than 8 shared code files simultaneously attached__

A maximum of 8 virtual memory addresses are available for shared code files; these slots have identifiers 1 to 8. In a future release this limit could be significantly increased, but the fundamental issue of needing a separate slot for each shared code file simultaneously will remain.

### Restriction 3

__Cannot `)SAVE` or `⎕SAVE` a workspace that has shared code files attached__

It is not possible to [`)SAVE`](../../language-reference-guide/system-commands/save.md) or [`⎕SAVE`](../../language-reference-guide/system-functions/save.md) the current workspace if any shared code files are attached (they must be [assimilated](../../../language-reference-guide/primitive-operators/i-beam/attach-assimilate-detach-shared-code-files/#assimilate-shared-code-files.md) or [detached](../../../language-reference-guide/primitive-operators/i-beam/attach-assimilate-detach-shared-code-files/#detach-shared-code-files.md) first).

### Restriction 4

__Attaching a shared code file containing namespaces copies all the namespaces (functions and arrays remain in the shared space)__

Attaching shared code files results in data being copied from the shared code files as needed. However, namespaces are always copied.

### Restriction 5

__Only certain content can be saved in a shared code files__

The content of a shared code file is limited to namespaces, nested arrays, simple arrays, tradfns, tradops, dfns, dops and derived functions (futures and external variables are instantiated and become arrays). If other content (for example, .NET objects, shared variables and COM objects) is present in a workspace then that workspace cannot be [saved](../../../language-reference-guide/primitive-operators/i-beam/save-shared-code-files/) as a shared code file.


## Summary of Limitations

Fundamental limitations:

- Shared code files are read only
- Shared code files have a fixed virtual memory address
- Shared code files cannot be shared across architectures
- Shared code files are not workspaces
- 64-bit Unicode only

Temporary limitations:

- All objects saved must be visible from the root of the current workspace
- It is not possible to have more than 8 shared code files simultaneously attached
- Cannot `)SAVE` or `⎕SAVE` a workspace that has shared code files attached
- Attaching a shared code file containing namespaces copies all the namespaces  (functions and arrays remain in the shared space)
- Only certain content can be saved in a shared code file

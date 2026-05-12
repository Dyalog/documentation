# Technical Details

xxx

## Technical Reference

The operations that comprise the shared code file mechanism are implemented using three I-Beams:

- `{R}←{X} (`[`8659⌶`](../../language-reference-guide/primitive-operators/i-beam/list-shared-code-files-attached-names)`) Y` – List Shared Code Files/Attached Names
	- list shared code files: `(8659⌶) ncs `
	- list attached names: `{slot} (8659⌶) ncs `
- `{R}←{X} (`[`8666⌶`](../../language-reference-guide/primitive-operators/i-beam/attach-assimilate-detach-shared-code-files)`) Y` – Attach/Assimilate/Detach Shared Code Files
    - attach shared code file: `{nameclasses} (8666⌶) file `
    - assimilate shared code files: `(8666⌶) ⎕NULL`
    - detach shared code files: `(8666⌶) 0⍴⊂''`
- `{R}←{X} (`[`8667⌶`](../../language-reference-guide/primitive-operators/i-beam/save-shared-code-files)`) Y` – Save Shared Code Files
    - save shared code file: `{names} (8667⌶) slot file`
	
The operations that comprise the shared code file mechanism are implemented using three I-Beams:

- [`8659⌶`](../../language-reference-guide/primitive-operators/i-beam/list-shared-code-files-attached-names) – List Shared Code Files/Attached Names
	- syntax: `{R}←{X}(8659⌶)Y`
	- options: 
	    - list shared code files: `(8659⌶) ncs `
	    - list attached names: `{slot} (8659⌶) ncs `
- [`8666⌶`](../../language-reference-guide/primitive-operators/i-beam/attach-assimilate-detach-shared-code-files) – Attach/Assimilate/Detach Shared Code Files
    - syntax: `{R}←{X}(8666⌶)Y`
	- options:
	    - attach shared code file: `{nameclasses} (8666⌶) file `
        - assimilate shared code files: `(8666⌶) ⎕NULL`
        - detach shared code files: `(8666⌶) 0⍴⊂''`
- [`8667⌶`](../../language-reference-guide/primitive-operators/i-beam/save-shared-code-files) – Save Shared Code Files
    - syntax: `{R}←{X}(8667⌶)Y`
    - options:
	    - save shared code file: `{names} (8667⌶) slot file`

## Technical Clarification

This section clarifies some of the functionality of shared code file support. Specifically:

- why shared code files are read-only

- the rules around attaching, assimilating, and detaching shared code files

### Shared Code Files are Read-Only

A shared code file is a read-only repository. Items within it can be modified, but doing so can result in data being copied into the main workspace.

Consider these cases where item `A` is modified:

- `A` is a function

    - `B←A` will introduce a new name `B` into the main workspace but no new data.
    - When `A` is edited or otherwise re-fixed, the new version will be stored in the main workspace.

- `A` is a simple array such as `1 2 3 4`

    - `B←A` will introduce a new name `B` into the main workspace but no new data.
    - `C←A,1` will introduce a new name `C` and new data into the main workspace.
    - `A,←1` will create new data in the main workspace.

- `A` is a nested array such as `'AB' 'CD'`

    - `B←A` will introduce a new name B into the main workspace but no new data.
    - `A[1]←⊂'XY'` will introduce some new data into the main workspace.

In each of these cases, the content of the attached shared code file remains unaltered. This means that, if names of items in a shared code file are expunged using [`⎕EX`](../../language-reference-guide/system-functions/ex) and the shared code file(s) are detached and reattached, then the items in the shared code file will be restored to their original values. The only way to change the values in a shared code file is to recreate the entire file.

Although a shared code files can contain data, these values should either be constants or initial values for structures that will be copied into the workspace as soon as the application modifies them.

### Attaching, Assimilating, and Detaching Shared Code Files

When one or more shared code files is attached, the following rules apply:

- When items with the same name exist in multiple workspaces, the one that is used in the active workspace is the first one found when going through the workspaces in the following order:
    1. the active workspace
    2. the shared code file specified first when [attaching](../../language-reference-guide/primitive-operators/i-beam/attach-assimilate-detach-shared-code-files#xxx))
    3. the shared code file specified second when attaching, and so so
- When the shared code files are assimilated:
    - all references to each shared code file are resolved by copying data from the shared code file to the active workspace as required.
- When the shared code files are detached:
    - names in the active workspace that reference data in a shared code file are deleted (namespace references are not deleted).
	- all remaining references to the shared code file are resolved by copying data from the shared code file to the active workspace as required.

<h4 class="example">Example</h4>

The active workspace MAIN is populated using the following assignments:
```apl
      FN1 ← {⍵ × 1}
      FN2 ← {⍵ × 2}
      NS1 ← ⎕NS ''
      NS1.A ← 1
```

|Name |Parent|Value        |
|-----|------|-------------|
|`FN1`|`#`   |`{⍵ × 1}`    |
|`FN2`|`#`   |`{⍵ × 2}`    |
|`NS1`|`#`   |Namespace ref|
|`A`  |`NS1` |`1`          |

Shared code files `DWS1` is populated using the following assignments:
```apl
      FN1 ← {⍵ × 1.1}
      FN3 ← {⍵ × 3}
      V ← 'AB' 'CD'
      NS1 ← ⎕NS ''
      NS1.A ← 2
      NS1.B ← 3

```

|Name |Parent|Value        |
|-----|------|-------------|
|`FN1`|`#`   |`{⍵ × 1.1}`  |
|`FN3`|`#`   |`{⍵ × 3}`    |
|`V`  |`#`   |`'AB' 'CD'`  |
|`NS1`|`#`   |Namespace ref|
|`A`  |`NS1` |`2`          |
|`B`  |`NS1` |`3`          |

Shared code files `DWS2` is populated using the following assignments:
```apl
      FN3 ← {⍵ × 3.1}
      FN4 ← {⍵ × 4}
      NS2 ← ⎕NS ''
      NS2.A ← 4
      NS3 ← ⎕NS ''
      NS3.A ← 5
```

|Name |Parent|Value        |
|-----|------|-------------|
|`FN3`|`#`   |`{⍵ × 3.1}`  |
|`FN4`|`#`   |`{⍵ × 4}`    |
|`NS2`|`#`   |Namespace ref|
|`A`  |`NS2` |`4`          |
|`NS3`|`#`   |Namespace ref|
|`A`  |`NS3` |`5`          |

After attaching `DWX1` and `DWX2` (in that order) to `MAIN` the following will be accessible:

|Name |Parent|Value        |Location of Value|Notes                                         |
|-----|------|-------------|-----------------|----------------------------------------------|
|`FN1`|`#`   |`{⍵ × 1}`    |`WS`             |`FN1` in `DWX1` is inaccessible               |
|`FN2`|`#`   |`{⍵ × 2}`    |`WS`             |&nbsp;                                        |
|`FN3`|`#`   |`{⍵ × 3}`    |`DWX1`           |`FN3` in `DWX2` in inaccessible               |
|`FN4`|`#`   |`{⍵ × 4}`    |`DWX2`           |&nbsp;                                        |
|`V`  |`#`   |`'AB' 'CD'`  |`DWX1`           |&nbsp;                                        |
|`NS1`|`#`   |Namespace ref|&nbsp;           |&nbsp;                                        |
|`A`  |`NS1` |`1`          |`WS`             |`NS1.A` and `NS1.B` in `DWX1` are inaccessible|
|`NS2`|`#`   |Namespace ref|&nbsp;           |&nbsp;                                        |
|`A`  |`NS2` |`4`          |`DWX2`           |&nbsp;                                        |
|`NS3`|`#`   |Namespace ref|&nbsp;           |&nbsp;                                        |
|`A`  |`NS3` |`5`          |`DWX2`           |&nbsp;                                        |

Following these assignments:
```apl
      FN3 ← {⍵ × 3.2}
      FN5 ← FN4
      V[1] ← ⊂'XY'
      NS2.B ← 6
```

The following are now accessible:

|Name |Parent|Value        |Location of Value            |Notes        |
|-----|------|-------------|-----------------------------|-------------|
|`FN1`|`#`   |`{⍵ × 1}`    |`WS`                         |&nbsp;       |
|`FN2`|`#`   |`{⍵ × 2}`    |`WS`                         |&nbsp;       |
|`FN3`|`#`   |`{⍵ × 3.2}`  |`WS`                         |Updated value|
|`FN4`|`#`   |`{⍵ × 4}`    |`DWX2`                       |&nbsp;       |
|`FN5`|`#`   |`{⍵ × 4}`    |`DWX2`                       |&nbsp;       |
|`V`  |`#`   |`'XY' 'CD'`  |Split between `WS` and `DWX1`|&nbsp;       |
|`NS1`|`#`   |Namespace ref|&nbsp;                       |&nbsp;       |
|`A`  |`NS1` |`1`          |`WS`                         |&nbsp;       |
|`NS2`|`#`   |Namespace ref|&nbsp;                       |&nbsp;       |
|`A`  |`NS2` |`4`          |`DWX2`                       |&nbsp;       |
|`B`  |`NS2` |`6`          |`WS`                         |New value    |
|`NS3`|`#`   |Namespace ref|&nbsp;                       |&nbsp;       |
|`A`  |`NS3` |`5`          |`DWX2`                       |&nbsp;       |

The shared code files are now disconnected. This is achieved either by assimilating them into the active workspace or by detaching them; the result of each of these operations is shown below.

Following assimilation of the shared code files, the main workspace will contain:

|Name |Parent|Value        |Notes                     |
|-----|------|-------------|--------------------------|
|`FN1`|`#`   |`{⍵ × 1}`    |&nbsp;                    |
|`FN2`|`#`   |`{⍵ × 2}`    |&nbsp;                    |
|`FN3`|`#`   |`{⍵ × 3.2}`  |&nbsp;                    |
|`FN4`|`#`   |`{⍵ × 4}`    |Copied into `WS`          |
|`FN5`|`#`   |`{⍵ × 4}`    |Copied into `WS`          |
|`V`  |`#`   |`'XY' 'CD'`  |Partially copied into `WS`|
|`NS1`|`#`   |Namespace ref|&nbsp;                    |
|`A`  |`NS1` |`1`          |&nbsp;                    |
|`NS2`|`#`   |Namespace ref|&nbsp;                    |
|`A`  |`NS2` |`4`          |Copied into `WS`          |
|`B`  |`NS2` |`6`          |&nbsp;                    |
|`NS3`|`#`   |Namespace ref|&nbsp;                    |
|`A`  |`NS3` |`5`          |Copied into `WS`          |

Alternatively, following detachment of the shared code files, the main workspace will contain the following values:

|Name |Parent|Value        |Notes                                   |
|-----|------|-------------|----------------------------------------|
|`FN1`|`#`   |`{⍵ × 1}`    |&nbsp;                                  |
|`FN2`|`#`   |`{⍵ × 2}`    |&nbsp;                                  |
|`FN3`|`#`   |`{⍵ × 3.2}`  |&nbsp;                                  |
|`FN5`|`#`   |`{⍵ × 4}`    |Copied into `WS`                        |
|`V`  |`#`   |`'XY' 'CD'`  |Partially copied into `WS`              |
|`NS1`|`#`   |Namespace ref|&nbsp;                                  |
|`A`  |`NS1` |`1`          |&nbsp;                                  |
|`NS2`|`#`   |Namespace ref|&nbsp;                                  |
|`A`  |`NS2` |`4`          |Copied into `WS` , namespace has changed|
|`B`  |`NS2` |`5`          |&nbsp;                                  |
|`NS3`|`#`   |Namespace ref                                        ||
|`A`  |`NS3` |`5`          |Copied into `WS`                        |

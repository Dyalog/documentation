# BuildGUI

Note: 

1. This code has been exported from the workspace `Core/ws/GUIMaint.dws`.
2. The code can only be run on Windows.

The main purpose of the code herein is to generate the crossreference tables present in the `Object Reference Guide`. In all likelihood, this is now fairly static, but changes do still happen. The code was written a long time ago, before Dyalog contained, for example, `⎕XML`.

The code has been left as-is, with the following exceptions:

1. The workspace has been exported to text, so that it can be versioned. 
2. The function `WriteFile.aplf` now ensures that any directories not present in its path are created.

Additionally, two new functions have been added:

1. `NewBuildGUI.aplf`: the new entry point, serving the same purpose as `BuildGUI.aplf`, but not writing entries into a Table of Contents file, and not writing stubbed entries of new object.
2. `NewWriteMembers.aplf`: analogous to `WriteMembers.aplf`, creating the actual crossreference tables, but writing Markdown instead of XML. This function will sort the tables it generates in col-major order. The old code generated tables that were occasionally not sorted at all.

To run this code, say

```apl
files ← NewBuildGUI '/some/path/to/your/project/dir/here'
```

Note that the old `BuildGUI.aplf` also takes a left arg 0 for "run" and 1 for "dry run". The old version was intended to write straight to the documentation repository, but we probably don't need to do that with the new one: write out the files to a fresh directory, do a diff against the existing, and integrate manually in the rare cases that something changed. 

## Platform audit

What note 2 above actually rests on, checked against the v21 documentation in this repository.

### Hard Windows-only

`⎕WC`, `⎕WG` and `⎕DQ` are documented Windows only (`language-reference-guide/docs/system-functions/wc.md`, `wg.md`, `dq.md`).

| File | Lines | Use |
|------|-------|-----|
| `MAKEALL.aplf` | 4 to 7 | `'.'⎕WG'ChildList'`, `'F'⎕WC'Form'` |
| `MAKE_PARENT.aplf` | 12, 13 | `'F'⎕WC'Form'` |
| `MAKE_INSTANCE.aplf` | 4 to 29 | every `:Case` branch is a `⎕WC`, plus `PARENT ⎕WG'Container'` |
| `ASK_PARENT.aplf` | 16 to 25 | `⎕WC` of Form, List and Button, then `⎕DQ'FF'` |

`MAKEALL.aplf:16-20` then reads `ref.PropList`, `ref.EventList`, `ref.MethodList` and `ref.ChildList`. These are properties of `⎕WC`-created objects and exist nowhere else. This is the premise of the whole tool: it discovers the object model by instantiating every object and asking the live interpreter what members it has. Not portable in principle, only replaceable.

`2031⌶0` at `BuildEvents.aplf:6` and `BuildMethods.aplf:6` supplies the event and method numbers. It does not appear in `language-reference-guide/docs/primitive-operators/i-beam/index.md`, so it is undocumented in v21 and carries no platform guarantee. What it returns is the Windows GUI event numbering.

`MAKE_INSTANCE.aplf:14`, `MAKEALL.aplf:4,6` and `ASK_PARENT.aplf:3-4` name COM, OLE and ActiveX classes (`OCXClass`, `OLEClient`, `NetControl`, `ActiveXContainer` and so on), which are Windows technologies. The five at line 14 are never instantiated: `MAKEALL.aplf:14` falls back to `#.ObjectMembers`.

### Windows conventions in strings and data

These run elsewhere without signalling, and produce wrong output.

Backslash path separators in `BuildGUI.aplf:21,22,26,53,152,161`, `WriteMembers.aplf:2,3`, `BuildProperties.aplf:13`, `BuildEvents.aplf:9`, `BuildMethods.aplf:9` and `ImportMethodsAndEvents.aplf:11,18`. Per `nparts.md`, "\" is a directory separator on Windows only. Elsewhere it is an ordinary filename character, so `3 ⎕MKDIR ⊃⎕NPARTS file` at `WriteFile.aplf:3` creates nothing useful and `⎕NCREATE` produces a single file named `Content\GUI\Objects\Button.htm` in the current directory.

Hard-coded CRLF at `indent.aplf:3`, `⎕AV[4 3]`. By `tc.md`, `⎕TC≡⎕AV[1+⍳3]` and `⎕TC` is backspace, linefeed, newline, so `⎕AV[3]` is LF and `⎕AV[4]` is CR. This also assumes `⎕IO←1`, which `indent` does not localise, and a default `⎕AVU`.

CRLF assumed on input: `BuildEvents.aplf:66`, `BuildMethods.aplf:65` and `BuildProperties.aplf:62` search for `'</div>',⎕UCS 13 10`. An LF file fails the `:ElseIf` and is silently left unmodified.

The ANSI branch in `WriteUnicodeFile.aplf:17-18`, `ReadFile.aplf:11` and `ReadxmlFile.aplf:12`. ANSI here means a Windows code page, and in the Classic Edition the byte to character mapping runs through `⎕AV` and the output translate table. Only the read side is still reachable: `WriteFile.aplf:4` always passes `'UTF-8'`.

### MadCap Flare output

The old path emits `.fltoc` and `.flsnp` files, the `CatapultToc` root element, the `MadCap:` namespace and the `Default.ScreenOnly` / `Default.PrintOnly` conditions. Flare is Windows-only software, so the output is unusable elsewhere even though the code producing it is portable. Confined to `BuildGUI`, `WriteMembers`, `BuildProperties`, `BuildEvents`, `BuildMethods` and `ImportMethodsAndEvents`.

### Portable despite appearances

`⎕USING←'System' 'System.IO'` at `BuildGUI.aplf:23` and `NewBuildGUI.aplf:10`. .NET is cross-platform in v21, and `dotnet-interface-guide/docs/installation.md` has `DYALOG_NETCORE` defaulting to `1` on Linux and macOS against `0` on Windows. It is also dead on the new path: nothing there resolves a .NET name.

The `(Windows)` comments at `ReadFile.aplf:2` and `WriteUnicodeFile.aplf:2` are inaccurate. `⎕NTIE`, `⎕NCREATE`, `⎕NAPPEND`, `⎕NREAD`, `⎕NSIZE`, `⎕NUNTIE` and `⎕NERASE` are all cross-platform, as are `⎕MKDIR`, `⎕NPARTS`, `⎕C`, `⎕R` and `⎕UCS`.

So the new Markdown path is already clean: `NewBuildGUI`, `NewWriteMembers`, `WriteFile` and `WriteUnicodeFile` use forward slashes, `⎕UCS 10` and UTF-8 throughout. Its only Windows dependency is the `MAKEALL` call at `NewBuildGUI.aplf:7`.

### Other gaps in this export

Not platform issues, but they stop the code running as checked in even on Windows.

- `Objects`, `#.ObjectMembers` (`MAKEALL.aplf:14`), `ExtractMethodOrEventDetails`, `ExtractList` and `ExtractDescription` (`ImportMethodsAndEvents.aplf:15,36,69`) are referenced but not exported.
- `ImportMethodsAndEvents` is unreachable. `BuildGUI` calls `BuildProperties`, `BuildEvents` and `BuildMethods` instead. It also references `d` and `indir`, neither of which is ever assigned.
- `WriteUnicodeFile.aplf:4` signals `DOMAIN ERROR` unless `⎕DR chars` is 80 or 160, so any character above U+FFFF (type 320) is rejected.
- `NewBuildGUI.aplf:13` computes `objfile` and never uses it. Lines 18, 33 and 37 build refs ending `.md"` with a stray double quote inherited from the HTML path, which `NewWriteMembers.aplf:12` strips again; line 29 omits it.
- The output shape no longer matches the guide. `NewBuildGUI` writes one file per object per member kind under `parentlists/`, `childlists/`, `proplists/`, `methodlists/` and `eventlists/`; `object-reference/docs/` has no such directories and carries the cross-references as inline link lists in each object page.

## Running it

1. Dyalog Unicode Edition for Windows.
2. `)LOAD Core/ws/GUIMaint.dws`. This directory is not self-contained. The global `Objects` and the namespace `#.ObjectMembers` (holding member lists for the classes that cannot be instantiated, such as `OCXClass` and `OLEClient`) live in the workspace.
3. Bring the `.aplf` files from this directory into the workspace, replacing the workspace copies.
4. `files ← NewBuildGUI '<output dir>'`, then diff `<output dir>` against `object-reference/docs/`.

`ASK_PARENT` opens a modal dialogue for any object whose parent is neither derivable from `ParentMap` nor in its hard-coded `:Case` list, so the run is not unattended.

## Caching the object model

`MAKEALL` sets five globals. Capturing them while on Windows removes the need for a Windows machine until the object model itself changes:

```apl
      MAKEALL
      model ← ⎕NS ⍬
      model.Objects ← Objects
      model.ParentMap ← ↓ParentMap    ⍝ JSON has no rank > 1
      model.(Properties Methods Events) ← Properties Methods Events
      ((1 ⎕JSON model) 'UTF-8' 10) ⎕NPUT 'objectmodel.json' 1
```

Restoring it anywhere:

```apl
      model ← 0 ⎕JSON ⊃⎕NGET 'objectmodel.json'
      Objects ← model.Objects
      ParentMap ← ↑model.ParentMap
      Properties Methods Events ← model.(Properties Methods Events)
```

`NewBuildGUI` calls `MAKEALL` unconditionally, so running from a cached model means dropping that call.

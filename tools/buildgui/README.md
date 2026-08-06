# BuildGUI

Originally the workspace `Core/ws/GUIMaint.dws`, now held as source: `.aplf` for the functions,
`.apla` for the two arrays it cannot regenerate. Used to generate the cross-reference tables in the
Object Reference Guide. It discovers the object model by instantiating every GUI object with `⎕WC`
and asking the live interpreter what members it has, so **it only runs on Windows**.

`objectmodel.json` in this directory is a capture of that model, so the discovery step does not have
to be repeated on every machine. Regenerate it only when the object model itself changes.

## Generating `objectmodel.json`

Requires Dyalog Unicode Edition **for Windows** (captured with 21.0.54393.0). This directory is
self-contained — it no longer needs `GUIMaint.dws`. Alongside the functions it holds `Objects.apla`
and `ObjectMembers/`, the global `Objects` and the namespace `#.ObjectMembers` (member lists for
classes that cannot be instantiated, such as `OCXClass` and `OLEClient`) exported as Link arrays.

1. **Load everything into a clear workspace.**

   ```apl
         )CLEAR
         ]LINK.Import # /path/to/tools/buildgui
   ```

   `Import` rather than `Create`: this is a one-shot load, and there is no reason to leave a watcher
   writing session changes back into the repository.

2. **Expose Root properties.**

   ```apl
         2401⌶1
   ```

   Not optional. `MAKE_INSTANCE` maps the Root object to `#`, so `MAKEALL` reads `#.PropList`, which
   does not resolve unless Root properties are exposed. This setting lives in the workspace rather
   than in code — the old `GUIMaint.dws` had it set, which is why it was invisible until the
   workspace was retired. Without it `MAKEALL` fails at line 15 with `VALUE ERROR: Undefined name:
   PropList`.

3. **Build the model.** This instantiates every object in turn, so windows flicker on the desktop.

   ```apl
         MAKEALL
   ```

   It sets five globals: `Objects`, `ParentMap`, `Properties`, `Methods` and `Events`.

4. **Serialise.**

   ```apl
         model ← ⎕NS ⍬
         model.Objects ← Objects
         model.ParentMap ← ↓ParentMap    ⍝ JSON has no rank > 1
         model.(Properties Methods Events) ← Properties Methods Events
         json ← 1 ⎕JSON⍠'Compact' 0⊢model
         lines ← (⎕UCS 13) (≠⊆⊢) json    ⍝ ⎕JSON separates lines with CR
         (lines 'UTF-8' 10) ⎕NPUT 'objectmodel.json' 1
   ```

   `⍠'Compact' 0` pretty-prints, one member per line, so that a regenerated model
   produces a readable diff instead of one changed 54 KB line. The split is needed
   because `⎕JSON` separates its lines with CR, which `⎕NPUT`'s LF line-ending
   argument does not recognise — write it without splitting and the whole file
   lands on a single line.

5. **Check the result** before committing. The v21.0 capture is 76 objects, a 76×76 `ParentMap`,
   2247 properties, 416 methods and 1105 events. A diff against the previous `objectmodel.json`
   should be empty unless the object model really changed.

## Using the cached model

```apl
      model ← 0 ⎕JSON ⊃⎕NGET 'objectmodel.json'
      Objects ← model.Objects
      ParentMap ← ↑model.ParentMap
      Properties Methods Events ← {0=≢⍵: 0⍴⊂'' ⋄ ⍵}¨¨ model.(Properties Methods Events)
```

The `{0=≢⍵: 0⍴⊂'' ⋄ ⍵}¨¨` is needed because JSON `[]` carries no element type. Seven member lists are
empty — `NetClient` has no properties, `NetClient` and `NetType` no methods, and those two plus
`OCXClass` and `OLEClient` no events — and they restore as empty character vectors (`⎕DR` 83) where
`MAKEALL` produced empty nested vectors (`⎕DR` 326). Both have shape 0, so it only matters to code
that compares with `≡`. With the normalisation the restore is `≡`-identical to a live `MAKEALL`.

`NewBuildGUI` calls `MAKEALL` unconditionally, so running from the cache means dropping that call.

## Auditing the guide against the model

`objref_audit.py` compares every cross-reference list, A-Z index and link in `object-reference/`
against `objectmodel.json`. Standard library only, no dependencies.

```sh
      python tools/buildgui/objref_audit.py                        # text report
      python tools/buildgui/objref_audit.py --markdown -o audit.md # markdown document
```

Exits 1 if it finds anything, 0 if clean, so it can gate CI. It applies the exclusion list below,
and knows about the deliberate exceptions — `index-property.md`, the Session (`⎕SE`) member pages,
`NetControl` — so a clean run means clean.

## Do not document these

`ShowSIP` (a method on 35 objects) and Form's `SIPMode`, `SIPResize` and `OKButton` are Windows
CE-era vestiges, deliberately excluded from the Object Reference Guide. They are present in the
interpreter's member lists and therefore in `objectmodel.json`. Anything generating documentation
from the model must filter them out.

## Gotchas

**New classes.** `MAKEALL` indexes `ParentMap` with `Objects⍳`, so any class returned by
`⎕WG'ChildList'` that is absent from `Objects` yields an index one past the end and signals
`INDEX ERROR`. v21 introduced `WCPlugin`, a child of both `Root` and `Form`, absent from `Objects`
and undocumented. Lines 4 and 6 therefore select with `∩Objects` rather than excluding known
non-objects by name, which keeps the model to the documented set and tolerates future additions. If
a new class *should* be documented, add it to `Objects` in the workspace rather than relaxing the
intersection.

**`ASK_PARENT`** opens a modal dialogue for any object whose parent is neither derivable from
`ParentMap` nor in its hard-coded `:Case` list. On the v21 model this branch is never reached and the
run completes unattended, but it remains a hazard if new objects appear.

**`NetControl`** is documented and present in `#.ObjectMembers` but missing from `Objects`, so it gets
no cross-reference tables.

## Why Windows only

`⎕WC`, `⎕WG` and `⎕DQ` are documented Windows-only
(`language-reference-guide/docs/system-functions/wc.md`, `wg.md`, `dq.md`).

| File | Lines | Use |
|------|-------|-----|
| `MAKEALL.aplf` | 4 to 7 | `'.'⎕WG'ChildList'`, `'F'⎕WC'Form'` |
| `MAKE_PARENT.aplf` | 12, 13 | `'F'⎕WC'Form'` |
| `MAKE_INSTANCE.aplf` | 4 to 29 | every `:Case` branch is a `⎕WC`, plus `PARENT ⎕WG'Container'` |
| `ASK_PARENT.aplf` | 16 to 25 | `⎕WC` of Form, List and Button, then `⎕DQ'FF'` |

`MAKEALL.aplf:16-20` reads `ref.PropList`, `ref.EventList`, `ref.MethodList` and `ref.ChildList`.
These are properties of `⎕WC`-created objects and exist nowhere else — the premise of the whole tool,
not portable in principle, only replaceable. `2031⌶0` at `BuildEvents.aplf:6` and
`BuildMethods.aplf:6` supplies the event and method numbers; it is undocumented in v21 and returns
the Windows GUI event numbering.

Everything downstream of `MAKEALL` is portable, which is what makes the cached model useful: the new
Markdown path (`NewBuildGUI`, `NewWriteMembers`, `WriteFile`, `WriteUnicodeFile`) uses forward
slashes, `⎕UCS 10` and UTF-8 throughout. Its only Windows dependency is the `MAKEALL` call at
`NewBuildGUI.aplf:7`. The old Flare path (`BuildGUI`, `WriteMembers`, `BuildProperties`,
`BuildEvents`, `BuildMethods`, `ImportMethodsAndEvents`) additionally hard-codes backslash separators
and CRLF, and emits `.fltoc`/`.flsnp` for MadCap Flare, which is itself Windows-only.

## Known defects in this export

Not platform issues, but they stop the code running as checked in even on Windows.

- `ExtractMethodOrEventDetails`, `ExtractList` and `ExtractDescription`
  (`ImportMethodsAndEvents.aplf:15,36,69`) are referenced but not exported.
- `ImportMethodsAndEvents` is unreachable — `BuildGUI` calls `BuildProperties`, `BuildEvents` and
  `BuildMethods` instead — and references `d` and `indir`, neither ever assigned.
- `WriteUnicodeFile.aplf:4` signals `DOMAIN ERROR` unless `⎕DR chars` is 80 or 160, rejecting any
  character above U+FFFF.
- `NewBuildGUI.aplf:13` computes `objfile` and never uses it. Lines 18, 33 and 37 build refs ending
  `.md"` with a stray double quote inherited from the HTML path, which `NewWriteMembers.aplf:12`
  strips again; line 29 omits it.
- The output shape no longer matches the guide. `NewBuildGUI` writes one file per object per member
  kind under `parentlists/`, `childlists/`, `proplists/`, `methodlists/` and `eventlists/`;
  `object-reference/docs/` has no such directories and carries the cross-references as inline link
  lists in each object page.

## Changes from the original workspace

1. Exported to text so it can be versioned.
2. `WriteFile.aplf` now creates any missing directories in its path.
3. `MAKEALL.aplf` lines 4 and 6 select children with `∩Objects` instead of blacklisting names — see
   "New classes" above.
4. Added `NewBuildGUI.aplf`, the entry point replacing `BuildGUI.aplf`, which does not write Table of
   Contents entries or stub entries for new objects.
5. Added `NewWriteMembers.aplf`, replacing `WriteMembers.aplf`, writing Markdown instead of XML and
   sorting the tables in col-major order. The old code produced tables that were sometimes unsorted.

# Namespaces

Namespace is a (class 9) object in Dyalog APL. Namespaces are analogous to
nested workspaces.
```apl
'Flat' APL Workspace      Workspace with Namespaces
.OLD-------------------.   .NEW-------------------.
|                      |   | FOO MAT VEC          |
| DISPLAY              |   | .Util----------.     |
|                      |   | |DISPLAY       |     |
|   FOO MAT VEC        |   | |...           |     |
|                      |   | '--------------'     |
|   WsDoc_Init         |   | .WsDoc-------------. |
|   WsDoc_Xref         |   | |Init .prt-..fmt--.| |
|   WsDoc_Tree         |   | |     |Init||line || |
|   WsDoc_prt_init     |   | |Tree |    ||     || |
|   WsDoc_current_page |   | |Xref |page||     || |
|   ...                |   | |     '----''-----'| |
|                      |   | '------------------' |
'----------------------'   '----------------------'
	
```

They provide the same sort of facility for workspaces as directories do for
filesystems. The analogy, based on DOS, might prove helpful:

|Operation        |Windows      |Namespace    |
|-----------------|-------------|-------------|
|Create           |mkdir        |`)NS or ⎕NS` |
|Change           |cd           |`)CS or ⎕CS` |
|Relative name    |dir1\dir\file|`NS1.NS2.OBJ`|
|Absolute name    |\file\file   |`#.NS.OBJ`   |
|Name separator   |\            |`.`          |
|Top (root) object|\            |`#`          |
|Parent object    |..           |`##`         |

## Namespaces bring a number of major benefits

They provide lexical (as opposed to dynamic) local names. This means that a
defined function can use local variables and functions which persist when it
exits and which are available next time it is called.

Just as with the provision of directories in a filing system, namespaces
allow us to organise the workspace in a tidy fashion. This helps to promote an
object oriented programming style.

## APL's traditional name-clash problem is ameliorated in several ways

- Workspaces can be arranged so that there are many fewer names at each namespace level. This means that when copying objects from saved workspaces there is a much reduced chance of a clash with existing names. 
- Utility functions in a saved workspace may be coded as a single namespace and therefore on being copied into the active workspace consume only a single name. This avoids the complexity and expense of a solution which is sometimes used in 'flat' workspaces, where such utilities dynamically fix local functions on each call.
- In flat APL, workspace administration functions such as `WSDOC` must share names with their subject namespace. This leads to techniques for trying to avoid name clashes such as using obscure name prefixes like `⍙⍙L1` This problem is now virtually eliminated because such a utility can operate exclusively in its own namespace.

## The programming of GUI objects is considerably simplified.

- An object's callback functions may be localised in the namespace of the object itself.
- Static variables used by callback functions to maintain information between calls may be localised within the object.

This means that the object need use only a single name in its namespace.

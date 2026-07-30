# <span>Dirty</span> <span>Property</span>

**Description**

The Dirty property indicates whether the current page is considered to have content (either because [`⎕WC`](../../../language-reference-guide/system-functions/wc-dyadic) has been used to write to it, or [PagesBeginDirty](pagesbegindirty.md) is set to `1`).

Dirty can be set to `1` to force an otherwise empty page to be printed (for example, if PagesBeginDirty has been set to `0`).

However, setting Dirty to `0` will not prevent a single page from being printed; the operating system does not allow the cancellation of a single page, only of the entire document.

**Application** 

Objects: [Printer](../objects/printer.md)

# <span>Dirty</span> <span>Property</span>

The Dirty property indicates whether the current page is considered to have content (either because [`⎕WC`](../../../language-reference-guide/system-functions/wc) has been used to write to it, or [PagesBeginDirty](pagesbegindirty.md) is set to `1`).

Dirty can be set to `1` to force an otherwise empty page to be printed (for example, if PagesBeginDirty has been set to `0`).

However, once a page has content, setting Dirty to `0` does not stop that page from being printed. The operating system does not allow an individual page to be cancelled; the only way to prevent a single page from being printed is to cancel the entire document.

## Application

Objects: [Printer](../objects/printer.md)

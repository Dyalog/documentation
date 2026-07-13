# APL Fonts

## Unicode Edition

The default font for the Unicode Edition is APL385 Unicode[^1] which is a TrueType font and is installed as part of Dyalog APL. APL385 Unicode is the font used to print APL characters in this manual. In principle, you may use any other Unicode font that includes the APL symbols.

## Classic Edition

In the Classic Edition, there are two types of APL font provided; bitmap (screen) and TrueType. There are also two different layouts, which are referred to as *Std* and *Alt*.

The bitmap fonts are designed for the screen alone and are named *Dyalog Std* and *Dyalog Alt*. The TrueType fonts have a traditional 2741-style italic appearance and are named *Dyalog Std TT* and *Dyalog Alt TT*<sup>1</sup>.

The *Std* layout, which was the standard layout for Versions of Dyalog APL up to Version 10.1 contains the APL underscored alphabet `Ⓐ-Ⓩ`. **The underscored alphabet is a deprecated feature and is only supported in this Version of Dyalog APL for backwards compatibility.**

The *Alt* layout, which replaced the *Std* layout as the standard layout for Version 12.0 Classic Edition onwards, does not have the underscored alphabet, but contains additional National Language characters in their place. Note that the extra National Language symbols share the same `⎕AV` positions with the underscored alphabet. If, for example, you switch from the *Std* font layout to the alternative one, you will see the symbol `Á` (A-acute) instead of the symbol `Ⓐ` (A-underscore).

You may use either a bitmap font or a TrueType font in your APL session (see [Session Operations](../../windows-ui-guide/session-toolbars) for details). You MUST use a TrueType font for printing APL functions.

[^1]: The Dyalog Std TT, Dyalog Alt TT, and APL385 Unicode fonts are the copyright of Adrian Smith.

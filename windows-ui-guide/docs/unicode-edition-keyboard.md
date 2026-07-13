# Unicode Edition Keyboard

## Introduction

Unicode Edition supports the use of standard Windows keyboards that have the additional capability to generate APL characters when the user presses Ctrl, Alt, AltGr (or some other combination of meta keys) in combination with the normal character keys.

Dyalog is supplied with the Dyalog Unicode IME keyboard for a range of different languages as listed below.  The intention is that only APL characters and characters that appear in locations different from the underlying keyboard are defined; any other keystroke is passed through *as is*.

## Installation

During the Installation of Dyalog Unicode Edition, setup installs the Dyalog Unicode IME (IME). For any given Input Language the IME consists of an additional service for that Input Language, and a translate table which maps keystrokes for the appropriate keyboard to Unicode code points for APL characters

An IME service is installed for every Input Language that the user who installs Dyalog has defined, as well as every Input Language for which Dyalog has support.

The keyboard mappings are defined for the following national languages: Belgian, Danish, Finnish, French, German, Italian, Spanish, Swedish, and British and American English.

These mappings are described at [https://dfns.dyalog.com/n_keyboards.htm](https://dfns.dyalog.com/n_keyboards.htm).

For any other Input Language the American English translate table is selected. Note that some Input Languages are defined to be *substitutes* for other Input Languages; for example Australian English Input is a substitute for American English Input, Austrian German Input a substitute for German German Input. In these cases the IME will install the appropriate translate table. It is also possible to create support for new languages or to modify the existing support. See the *IME User Guide* for further details.

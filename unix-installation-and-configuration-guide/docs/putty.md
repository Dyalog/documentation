# Using PuTTY under Windows

Dyalog APL for UNIX comes with support for the PuTTY terminal emulator. PuTTY is freely downloadable, supports ssh and telnet protocols, and supports Unicode keystrokes and fonts. To be able to generate and see APL characters it is also necessary to install the Dyalog UnicodeIME and the APL385 Unicode font.

## Downloading and installing the Dyalog UnicodeIME

The UnicodeIME can be freely downloaded from https://www.dyalog.com/apl-font-keyboard.htm. It is also included with all Unicode Windows versions of Dyalog from 13.0 onwards. There are two versions of the UnicodeIME; one for 32 bit Windows, and one for 64 bit; please ensure that the correct version is downloaded.

Details of how to install the UnicodeIME are on the download webpage.

## Downloading and installing the APL385 font

The APL385 can be freely downloaded from https://www.dyalog.com/apl-font-keyboard.htm. Details of how to install the font appear on the download webpage.

## Downloading and Installing PuTTY

PuTTY is available from https://www.chiark.greenend.org.uk/~sgtatham/putty. Full details of how to download and install PuTTY, along with the licence terms and conditions are available from the above URL.

## Configuring PuTTY to support Dyalog APL for UNIX

Firstly ensure that you are able to login to the UNIX server which has Dyalog APL installed on it. If you are using an AIX server, it is recommended that in the Keyboard category you set the backspace key to Control-H.

For APL support the follow settings are required:

*Window/Appearance Font settings/Font:* set to *APL385 Unicode*

*Window/Translation/Character set translation on received data:* set *Received data assumed to be in which character set* to *UTF-8*

You should ensure that *Terminal/Keyboard/The Backspace key* is set appropriately for the remote operating system. AIX defaults to Ctrl-h whereas most other operating systems default to Ctrl-?

Having set these values, it is recommended that you save the settings; if you will need to connect to multiple servers, it is recommended that you save the above settings as the default options (Highlight the "*Default Settings*" in *Saved Sessions* and click on *Save*).

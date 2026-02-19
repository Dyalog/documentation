<h1 class="heading"><span class="name">Configuring a Console/terminal Window to support Dyalog APL for UNIX</span></h1>

In order to support Dyalog APL for UNIX in a console/terminal window under a Linux window manager, it is necessary to install and configure the Dyalog APL keyboard support. Additionally it is possible to install the APL385 Unicode font, to be used instead of the built in fonts which include APL characters.

## Keyboard support

Dyalog submitted APL Language keyboard support to Xorg at the end of 2011; most Linux distributions released after mid-2012 have the Dyalog APL keyboard support included with the distribution. Such distributions include openSUSE 12.2, Ubuntu 12.10 and Fedora 17.

Support for the Behind character was submitted to Xorg in late-2024; if your distribution does not support this character, contact Dyalog support for assistance.

Details of how to configure the keyboard under KDE4 appear below; keyboard support for other window managers (such as Gnome and Unity) is in a state of flux. The latest information about the process of installing and configuring Dyalog APL keyboard support for such environments can be found at:

https://www.dyalog.com/forum/viewtopic.php?f=20&t=210

or by contacting Dyalog support. The same resources can be used to obtain information and guidance on installing keyboard support for earlier Linux distributions.

## Configuring the APL keyboard under KDE4

(These instructions were drawn up using openSUSE 12.2; other KDE4 environments may vary slightly)

- Select Configure Desktop
- Select Input Devices
- Select Keyboard
- Select Layouts
- Select the "Configure layouts" tickbox
- Select Add
- In the Add Layout dialog box, select the Layout "APL Keyboard Symbols", and then the "dyalog"  option
- Close the Add Layout dialog box
- The list of layouts should now include APL Keyboard Symbols, with one of the dyalog variants.
- Click on "Main shortcuts" in the "Shortcuts for Switching Layout" group; where possible, Dyalog recommends selecting "Any Win key (while pressed)" so that either Windows key causes APL characters to be generated.

## APL font support

APL characters are available under Linux window managers. However some of the characters may appear inelegant; most noticeable are very small "`⋄`" and overly large "`⌶`". To resolve this, it is possible to use the Freemono fonts (these are installed by default on some distributions (such as openSUSE)), or to download and install the APL385 Unicode font. This font is freely downloadable from:

[https://www.dyalog.com/apl-font-keyboard.htm](https://www.dyalog.com/apl-font-keyboard.htm)

Details of how to install the font will appear in the documentation for your window manager.

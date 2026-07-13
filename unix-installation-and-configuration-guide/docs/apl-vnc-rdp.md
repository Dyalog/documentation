# Dyalog APL, RDP and VNC

Due to the different ways that Microsoft Windows and Linux/UNIX handle keyboards, it is not possible to use RDP or VNC or X-Windows from a Windows client to control a Dyalog APL session running under a UNIX window manager. In particular, all of the X-Window clients that Dyalog is aware of do not  fully support xkb key mappings.

It is possible to use VNC from a Linux client to connect to a remote Linux desktop and control an APL session running there; the keyboard support will however need to be added to the local machine.

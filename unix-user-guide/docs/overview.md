<h1 class="heading"><span class="name">Overview</span></h1>

Dyalog APL was originally written for use with serially attached character based terminals, which had a fixed-sized viewing window, and a limited number of keystrokes.

This tty version is now usually run using either a terminal window in a GUI-based windows manager, or a terminal emulation application such as PuTTY. Although these allow for a greater range of keystrokes, and for the resizing of the terminal window in which Dyalog APL is running, they still emulate the original ASCII terminals, so the same techniques for controlling the display still apply.

Note: From Version 14.1 onwards Dyalog [Ride](https://dyalog.github.io/ride) (Remote-IDE) can be used as the front-end for Dyalog running on any platform; Ride itself is currently supported on Windows, Linux and macOS. For macOS, Ride is the default front-end for Dyalog, and is documented in [https://dyalog.github.io/ride](https://dyalog.github.io/ride). Ride can be downloaded from [https://my.dyalog.com](https://my.dyalog.com/). Be aware that Ride 2.0 works only with version 14 interpreters, and that Ride 3 works only with version 15.0 interpreters onwards. Dyalog intends that this will be the last time that such an incompatibility will be introduced.

It is possible to support most terminals or terminal emulators with the Dyalog APL tty version, and it is possible for any user to define their own input translate table so that the keystrokes to enter commands or characters can be unique to their environment (similarly the output translate table defines the colour scheme etc.). As such, this document does not in general refer to the actual keystrokes which are used to control Dyalog APL, but rather the keycodes to which keystrokes are mapped.

Indeed, much of the interface to Dyalog APL can be customised; this manual is written assuming that no changes have been made to the default configuration.

Appendix A lists the mapping between keystrokes and keycodes for all commands used when running under a terminal emulator/console under Linux; Appendix B lists the keystrokes and keycodes used when running PuTTY, a windows terminal emulator. Some keycodes are not relevant to the current tty versions of Dyalog APL; they may have been used in previous tty versions, or used in versions no longer supported, or are used in GUI-based versions of Dyalog APL. They are listed for completeness in Appendix C, but attempting to make use of them may lead to unexpected and/or undesirable results.

The keyboard is used for two purposes: to enter text and to enter commands. In classic editions text is limited to characters defined in `⎕AV`, in Unicode editions text can consist of any valid Unicode character. The main issue which has to be resolved is how to locate these characters and commands on the keyboard in such a way that they can be entered in a consistent manner, and without conflicts with other characters or functionality.

Given that the number of different characters and commands far exceeds the number of keys on a keyboard, different methods are supported for allowing one key to be used for more than one character or command. There are three methods that can be used, and that can be combined:

1. Use a **metakey** with the keystroke. The metakey is held down at the same time as the key to be pressed. Examples of metakeys are the Shift key, the Control (Ctrl) key and the Windows Key (WindowsKey).
2. Define multiple modes for the keyboard. Certain keystrokes are reserved for swapping between modes; the effect of hitting any other key differs depending on the current mode. This was extensively used for earlier versions of Dyalog APL, which used Ctrl-o and Ctrl-n to swap between ASCII and APL entry modes.
3. Define multiple temporary modes for the keyboard, those modes last for one keystroke only. This is used for entering many commands in the tty version.

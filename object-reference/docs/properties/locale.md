# <span>Locale</span> <span>Property</span>

**Description**

The Locale property specifies the language in which the OLE server, attached to an OLEClient, exposes its methods (functions) and properties (variables).

When you create an OLEClient object, Dyalog APL/W requests the default Type Library associated with the OLE server that you specify. Many OLE servers, such as Excel.Application, provide different names for the methods and properties they expose for different languages. Without Locale, it would be difficult to write an OLE client application that could run in different countries, as the names of the functions and variables may be unpredictable.

Locale is an integer; for example, the value 9 specifies English and the value 12 specifies French.

Locale may **only** be specified by the `⎕WC` statement that is used to create the OLEClient; it may not subsequently be changed using `⎕WS`. A table of commonly used Locale values is given below.

Note that Dyalog cannot guarantee that you will actually be given the Locale you specify. This is a function of your specific installation and the OLE server in question. However, Dyalog believes that for Microsoft products, it is a fairly safe bet that the US/English interface will be available in most countries.

|Language  |Locale|
|----------|------|
|Neutral   |0     |
|Danish    |6     |
|Dutch     |19    |
|English   |9     |
|Finnish   |11    |
|French    |12    |
|German    |7     |
|Italian   |16    |
|Norwegian |20    |
|Portuguese|22    |
|Russian   |25    |
|Spanish   |10    |
|Swedish   |29    |

**Application**

Objects: [OLEClient](../objects/oleclient.md)

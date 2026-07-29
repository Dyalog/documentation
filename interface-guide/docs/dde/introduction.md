# Introduction to DDE

Dynamic Data Exchange (DDE) is a protocol supported by Microsoft Windows that enables two applications to communicate with one another and to exchange data.

DDE has largely been superseded by COM, but continues to be supported by Dyalog APL for backwards compatibility. For new applications, use COM.

Two applications exchange information by having a **conversation**. In any conversation, there is a **client**, which is the application that initiates the conversation, and a **server**; the application that is responding to the client. An application may partake in several conversations at the same time, and may play the server role in some and the client role in others. Indeed, it is perfectly reasonable for two applications to have two conversations in which each acts as the server in one and the client in another.

Most conversations are effectively *one-way* in that data flows from the server to the client. However, conversations are potentially bi-directional and it is possible for the client to send data to the server. This is often described as *poking* data.

To initiate a DDE conversation, the client application must specify the name of the server and the subject of the conversation, called the **topic**. The combination of application and topic uniquely identifies the conversation. In most applications that support DDE, the topic is the "document name". For example, Microsoft Excel recognises the name of a spreadsheet file (.XLS or .XLC) as a topic.

During a conversation, the client and server exchange information concerning one or more **items**. An item identifies a particular piece of data. For example, Microsoft Excel recognises cell references (such as R1C1) as data **items** in a conversation. Throughout a conversation, the client may specify how it wishes to be updated when the data in the server changes.

There are three alternatives. Firstly, the client can explicitly request the value of an item as and when it needs it. This is described as a **cold link**. Alternatively, a client may ask the server to supply it with the value of a particular item whenever its value changes. This is called a **hot link**.  Finally, it may ask the server to **notify** it whenever the value of an item changes, to which the client may respond by asking for the new value or not. This is termed a **warm link**.

In addition to providing a means for exchanging **data**, DDE provides a mechanism for one application to instruct another application to **execute** a command. This is implemented by sending a DDE_EXECUTE message. It is important to understand that the effect of the command is local to the application in which it is executed, and that the recipient of the message does **not** return a result to the originating application. It does **not** work like the APL execute function.

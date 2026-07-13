# Configuring an out-of-process OLEServer for DCOM

## Introduction

When you register an *out-of-process* OLEServer using *File/Export* or OLERegister, Dyalog APL automatically updates the Windows registry so that your OLEServer is immediately accessible to an OLE client application running on *the same* computer.

If you wish to make the same object accessible to client applications running on *different* computers (using distributed COM, or DCOM) you have to install additional registry entries on the server and on each of the clients.

Once you have established these registries entries, you should be able to access the OLEServer from Windows 95 or NT client computers in exactly the same way as if it were local; the client applications need not know where the server is located. In most cases, these additional registry entries are sufficient. However, the NT and DCOM security considerations may require the use of `dcomcnfg.exe` (a Microsoft utility) to set additional values. For example, if you get `E_ACCESSDENIED` errors when connecting from the client you may need to run `dcomcnfg.exe` on the server computer to assign the appropriate launch and access permissions for the OLEServer object.

The additional registry entries are described below. You may add these to the registry directly (using `regedit.exe`) or by running the functions provided in the `DCOMREG.DWS` workspace.

## DCOM Registry Entries for the Server

On the computer upon which you want the OLEServer to be run, you must add the following registry entries.

1. A key under `HKEY_CLASSES_ROOT\AppID` whose name corresponds to the CLSID of your OLEServer object as reported by the value of its `ClassID` property. The *(Default)* value of this key should be the name of the server object. In addition, you must define a *RunAs* entry which specifies the manner in which a client application runs your server. The simplest choice is *Interactive User* which specifies that the client application is treated like a normal user.
    
    For example, if you had saved an OLEServer namespace called `Loan` (c.f. `samples\loan.dws`), whose `ClassID` property had the value `{B80E9D40-2090-11D1-8F93-0020AFABD95D}` the entries would be:
    ```
    HKEY_CLASSES_ROOT\AppID\{B80E9D40-2090-11D1-8F93-0020AFABD95D}
    (Default)=dyalog.Loan
    RunAs=Interactive User
    ```
   
1. An AppID entry to the `HKEY_CLASSES_ROOT**\**CLSID` key. (Note that this key will itself have been created by Dyalog APL/W when you saved the workspace) Once again, CLSID refers to the value of your OLEServer's `ClassID` property. The value of the AppID entry is the (same) CLSID. Using the same example as above, the entry would be:
    ```
    HKEY_CLASSES_ROOT\{B80E9D40-2090-11D1-8F93-0020AFABD95D}
    AppID={B80E9D40-2090-11D1-8F93-0020AFABD95D}
    ```

## DCOM Registry Entries for the Client

On each of the computers from which you wish to call the OLEServer object as a client, you must add the following entries.

1. Two keys under `HKEY_CLASSES_ROOT` that identify the object (locally) and associate it with your OLEServer Note that the local name of the object is arbitrary and may be different on each client.
    ```
    HKEY_CLASSES_ROOT\dyalog.ServerName</p>
    HKEY_CLASSES_ROOT\dyalog.ServerName\CLSID
    ```
    CLSID is again the CLSID of the OLEServer object (this **must** be the same as that of the server machine). `dyalog.ServerName` can be replaced with whatever name you want clients to use to refer to this object.

1. Under `HKEY_CLASSES_ROOT\AppID`, a key whose name corresponds to the CLSID of your server object. The *(Default)* value of this key should be the name of the OLE server object (its name on the server computer). In addition, the key should contain a *RemoteServerName* entry whose value is the name of the server computer. For example:
    ```
    HKEY_CLASSES_ROOT\AppID\{B80E9D40-2090-11D1-8F93-0020AFABD95D}
    (Default)=dyalog.Loan
    RemoteServerName=ntsvr
    ```

## DCOMREG Workspace

The workspace DCOMREG.DWS contains a single namespace called `reg` that contains three functions to help register an *out-of-process* OLE Server for DCOM.

## RegDCOMServer

This function should be run on the *server* computer and is called as follows:
```apl
      RegDCOMServer ServerName CLSID
```

Where `ServerName` is a character string containing the (full) name of the OLEServer (e.g. `dyalog.Loan`) and `CLSID` is a character string containing the CLSID of the server (the value of it `ClassID` property). For example:
```apl
      )LOAD LOAN
.\LOAN saved ...
      )COPY DCOMREG
DCOMREG saved ...
 
      CLSID ←('Loan' ⎕WG 'ClassID')
      reg.RegDCOMServer 'dyalog.Loan' CLSID
```

## RegDCOMClient

This function should be run on each of the *client* computers and is called as follows:
```apl
      machine RegDCOMClient ServerName CLSID
```

Where `machine` is a character vector specifying the name of the (NT) server computer, `ServerName` is a character vector containing the (full) name of the OLEServer (e.g. `dyalog.Loan`) and `CLSID` is a character string containing the CLSID of the server (the value of it `ClassID` property). For example:
```apl
      CLSID←'{B80E9D40-2090-11D1-8F93-0020AFABD95D}'
      'NTSVR' reg.RegDCOMClient 'dyalog.Loan' CLSID
```

## Config

This niladic function simply invokes the `dcomcnfg.exe` utility using `⎕CMD`.

<h1 class="heading"><span class="name">Files and Directories</span></h1>

## Unicode and Classic Editions

Dyalog is available in two separate editions:  

* The _Unicode_ edition is Dyalog’s strategic edition; it is the edition that is generally available, and the only one available to new users. It is compatible with many third-party applications and tools, is capable of handling data from third-party tools and websites, and can be used with source code management systems (such as Git) to store APL code.
* The _Classic_ edition is only available for existing customers who have been using Dyalog for a long time and for whom moving to the Unicode edition would involve considerable effort.

## 32-Bit and 64-Bit Widths

Two separate widths of Dyalog for Microsoft Windows are available. The 32-bit width  will run on both 32-bit and 64-bit operating systems; the 64-bit width will only run on a 64-bit operating system.

## Files

The names of the files that are included in a Dyalog installation can vary slightly between the different editions and widths.

For information about licences, see [https://www.dyalog.com/prices-and-licences.htm](https://www.dyalog.com/prices-and-licences.htm) or contact sales@dyalog.com.

### Distributable Development Components

This section lists the files that are included with Dyalog for Microsoft Windows that can be distributed as part of end-user applications, under the terms and conditions of your Dyalog Run-Time Licence or Royalty Licence.

The following files have names that are consistent between editions; differences in names for the different widths are indicated by **&lt;width>**, which can be either **32** or **64**):  

* **dyascript.exe**
* **dyalogrt.exe**
* **dyalog&lt;width>.dll**
* **dyares{{ version_condensed }}_&lt;width>.dll**
* **dyalogprovider.dll** (.NET Framework Interface)
* **dyalognet.dll** (.NET Framework Interface)
* **conga{{ conga_version_condensed }}ssl&lt;width>.dll** (Conga and Ride)
* **conga{{ conga_version_condensed }}_&lt;width>.dll** (Conga and Ride)
* **exestub.dll**
* **dllstub.dll**
* **sqapl.ini**
* **sqapl.err**
* **aplunicd.ini**
* **sharpplot.dll**
* **sharpplot.xml**

The following files relate to the .NET Interface, and are only available in Unicode editions:  

* **Dyalog.Net.Bridge.Host.Windows.dll**
* **Dyalog.Net.Bridge.dll**
* **Dyalog.Net.Bridge.deps.json**
* **Dyalog.Net.Bridge.runtimeconfig.json**

The following files have names that change between editions and widths:  

* 64-bit Unicode:  
    * **dyalog{{ version_condensed }}_64rt_unicode.dll**
    * **bridge{{ version_condensed }}-64_unicode.dll**
    * **dyalogc64_unicode.exe**
    * **cwdya64u64w.dll**
* 32-bit Unicode:  
    * **dyalog{{ version_condensed }}rt_unicode.dll**
    * **bridge{{ version_condensed }}_unicode.dll**
    * **dyalogc_unicode.exe**
    * **cwdya64u32w.dll**
* 64-bit Classic:  
    * **dyalog{{ version_condensed }}_64rt.dll**
    * **bridge{{ version_condensed }}-64.dll**
    * **dyalogc64.exe**
    * **cwdya64c64w.dll**
* 32-bit Classic:  
    * **dyalog{{ version_condensed }}rt.dll**
    * **bridge{{ version_condensed }}.dll**
    * **dyalogc.exe**
    * **cwdya64c32w.dll**

### Non-Distributable Development Components

The following files are included with Dyalog for Microsoft Windows. These files must not be distibuted without an appropriate licence:  

* **dyalog.exe**
* **dyalog{{ version_condensed }}_&lt;width>.dll** or **dyalog{{ version_condensed }}_&lt;width>_unicode.dll**          

## File Extension Conventions

The following file extension conventions have been adopted for the various files distributed with, and used by, Dyalog.

|Extension|Description                     |
|---------|--------------------------------|
|**.dws**     |Dyalog workspace            |
|**.dse**     |Dyalog Session              |
|**.dcf**     |Dyalog component file       |
|**.DXV**     |Dyalog external variable    |
|**.din**     |Dyalog input table          |
|**.dot**     |Dyalog output table         |
|**.dft**     |Dyalog format file          |
|**.DXF**     |Dyalog transfer file        |
|**.dlf**     |Dyalog Session log file     |
|**.dyalog**  |Dyalog SALT file            |
|**.dyapp**   |Dyalog SALT application file|

!!! Info "Information"
    Some of these extensions (notably **.dcf**, **.dlf**, **.dot**, and **.DXF**) are not unique to Dyalog, and conflict with the same extensions used by other software applications. Although all the above file extensions are associated with Dyalog during its installation, these associations could subsequently be changed by the installation of other software or by a Microsoft Windows System restore.

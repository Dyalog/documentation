<h1 class="heading"><span class="name">Non-Modal Forms</span></h1>

Non-modal Forms are displayed using the `Run` method of the `System.Windows.Forms.Application` object. This method is designed to be called once, and only once, during the life of an application and this poses problems during APL development. Fortunately, it turns out that, in practice, the restriction is that `Application.Run` may only be run once on a single system thread. However, it may be run successively on different system threads. During development, you may therefore test a function that calls `Application.Run`, by running it on a new APL thread using Spawn (`&`). See Chapter 13 for further details.

## DataGrid Examples

Three functions in the `samples\winforms\winforms.dws` workspace provide examples of non-modal Forms. These examples also illustrate the use of the WinForms.DataGrid class.

Function `Grid1` is an APL translation of the example given in the help file for the DataGrid class in the .NET SDK Beta1. The original code has been slightly modified to work with the current version of the SDK.

Function `Grid2` is an APL translation of the example given in the help file for the DataGrid class in the .NET SDK Beta2.

Function `Grid` is an APL translation of the example given in the file:
```apl
C:\Program Files\Microsoft.NET\SDK\v1.1\...
QuickStart\winforms\samples\Data\Grid\vb\Grid.vb
```

This example uses Microsoft SQL Server 2000 to extract sample data from the sample NorthWind database. To run this example, you must have SQL Server running and you must modify function `Grid_Load` to specify the name of your server.

## GDIPLUS Workspace

The `samples\winforms\gdiplus.dws` workspace contains a sample that demonstrates the use of non-rectangular Forms. It is a direct translation into APL from a C# sample (WinForms-Graphics-GDIPlusShape) that was distributed on the Visual Studio .NET Beta 2 Resource CD.

## TETRIS Workspace

The `samples\winforms\tetris.dws` workspace contains a sample that demonstrates the use of graphics. It is a direct translation into APL from a C# sample (WinForms-Graphics-Tetris) that was distributed on the Visual Studio .NET Beta 2 Resource CD.

## WEBSERVICES Workspace

An example of a non-modal Form is provided by the `WFGOLF` function in the `samples\asp.net\webservices\webservices.dws` workspace. This function performs exactly the same task as the `GOLF` function in the same workspace, but it uses Windows.Forms instead of the built-in Dyalog GUI.

`WFGOLF`, and its callback functions `WFBOOK` and `WFSS` perform exactly the same task, with almost identical dialog box appearance, of `GOLF` and its callbacks `BOOK` and `SS` that are described in Chapter 7.

Note that when you run `WFGOLF` or `GOLF` for the first time, you must supply an argument of 1 to force the creation of the proxy class for the `GolfService` web service.
